import requests
from bs4 import BeautifulSoup
from newspaper import Config, Article
import re
import json



# Function to extract links from a webpage
def extract_links(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    links = [link.get('href') for link in soup.find_all('a', href=True)]
    return links

# Function to extract titles and descriptions from articles on a webpage
def extract_articles_info(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    articles = []
    # Check if the webpage follows a specific structure
    if 'dawn.com' in url:
        # For dawn.com
        article_elements = soup.find_all('article')
        for article in article_elements:
            # Check if each article contains 'h2' and 'p' tags
            title_element = article.find('h2')
            description_element = article.find('p')
            if title_element and description_element:
                title = title_element.text.strip()
                description = description_element.text.strip()
                articles.append({'title': title, 'description': description})
    elif 'bbc.com' in url:
        # For bbc.com
        article_elements = soup.find_all('div', class_='media__content')
        for article in article_elements:
            # Check if each article contains 'h3' and 'p' tags
            title_element = article.find('h3')
            description_element = article.find('p')
            if title_element and description_element:
                title = title_element.text.strip()
                description = description_element.text.strip()
                articles.append({'title': title, 'description': description})
    return articles


# Function to extract titles and descriptions from articles using newspaper3k
def extract_articles_info_newspaper(url):
    # Configuration to improve extraction success rate
    config = Config()
    config.browser_user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'
    article = Article(url, config=config)
    article.download()
    article.parse()
    title = article.title
    description = article.meta_description
    return {'title': title, 'description': description}



# Function for text preprocessing
def preprocess_text(text):
    # Check if input is a dictionary
    if isinstance(text, dict):
        # If it's a dictionary, preprocess the 'title' key
        return {'title': text['title'], 'description': text['description']}
    # If it's a string, preprocess the string
    # Remove special characters and digits
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    # Convert to lowercase
    text = text.lower()
    # Remove extra whitespaces
    text = ' '.join(text.split())
    return text


# Function to save data to a JSON file
def save_to_json(data, filename):
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)  # Indent for pretty formatting
        
        

# URLs of dawn.com and bbc.com
dawn_url = 'https://www.dawn.com/'
bbc_url = 'https://www.bbc.com/'

# Extracting links from the landing pages
dawn_links = extract_links(dawn_url)
bbc_links = extract_links(bbc_url)

# Extracting articles using newspaper3k
dawn_articles_info = extract_articles_info_newspaper(dawn_url)
bbc_articles_info = extract_articles_info_newspaper(bbc_url)

# Printing extracted data for verification
print("Dawn Links:", dawn_links)
print("BBC Links:", bbc_links)
print("Dawn Articles Info:", dawn_articles_info)
print("BBC Articles Info:", bbc_articles_info)


# Preprocess titles and descriptions
preprocessed_dawn_article_info = preprocess_text(dawn_articles_info)
preprocessed_bbc_article_info = preprocess_text(bbc_articles_info)

# Printing preprocessed data for verification
print("Preprocessed Dawn Article Info:", preprocessed_dawn_article_info)
print("Preprocessed BBC Article Info:", preprocessed_bbc_article_info)


# Save preprocessed data to JSON files
save_to_json(preprocessed_dawn_article_info, "preprocessed_dawn_articles_info")
save_to_json(preprocessed_bbc_article_info, "preprocessed_bbc_articles_info")

