import requests
from bs4 import BeautifulSoup
from newspaper import Config, Article
import re
import json


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