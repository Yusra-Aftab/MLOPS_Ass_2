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
