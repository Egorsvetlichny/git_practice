# Использование BeautifulSoup для скрапинга

from bs4 import BeautifulSoup
import requests

url = 'http://example.com/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
print(soup)
