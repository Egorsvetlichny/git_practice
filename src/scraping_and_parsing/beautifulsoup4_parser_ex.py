#  BeautifulSoup - инструмент специально разработан для парсинга HTML-кода (в отличие от regex и xpath)

# В приведенном ниже примере из исходного кода страницы извлекаются уникальные ссылки, за исключением внутренних.

import requests
from bs4 import BeautifulSoup

url = 'https://webscraper.io/test-sites/e-commerce/allinone/phones'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
links = set()

for link in soup.find_all('a'):
    l = link.get('href')
    if l is not None and l.startswith('https'):
        links.add(l)

for link in links:
    print(link)
