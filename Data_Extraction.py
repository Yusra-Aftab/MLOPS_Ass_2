import requests
from bs4 import BeautifulSoup
from newspaper import Config, Article
import re
import json
from preprocess_data import preprocess_text
from extract_data import extract_links, extract_articles_info_newspaper
from save_to_json import save_to_json
        

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

