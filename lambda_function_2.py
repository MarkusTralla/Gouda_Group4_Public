from bs4 import BeautifulSoup
import json
import urllib.request
from urllib.request import urlopen
import time

def lambda_handler(event, context):
    urls = [
    'https://www.cheese.com/abbaye-de-belloc/',
    'https://www.cheese.com/abbaye-de-belval/',
    'https://www.cheese.com/abbaye-de-citeaux/',
    'https://www.cheese.com/tamie/',
    'https://www.cheese.com/abbaye-de-timadeuc/',
    'https://www.cheese.com/abbaye-du-mont-des-cats/',
    'https://www.cheese.com/abbots-gold/',
    'https://www.cheese.com/abertam/',
    'https://www.cheese.com/abondance/',
    ]
    
    for url in urls:
        page = urllib.request.Request(url)
        response = urllib.request.urlopen(page)
        page_html = response.read()
        page_soup = BeautifulSoup(page_html, "html.parser")
        for summary_traits in page_soup.find_all('ul', class_="summary-points"):
            print(summary_traits.text)