# Использование регулярных выражений для парсинга. Парсинг нужной ссылки из html разметки сайта

import re

from bs4 import BeautifulSoup
import requests

url = 'http://example.com/'
response = requests.get(url)
soup = str(BeautifulSoup(response.text, 'html.parser'))
regex = r'<a\s+href=["\'](?P<link>[^"\']+)["\']>'
links = re.findall(regex, soup)
print(*links)
