# Язык запросов XPath (XML Path Language) позволяет извлекать данные из определенных узлов XML-документа.
# Для работы с HTML кодом в Python используют модуль html из библиотеки lxml

from lxml import html

from bs4 import BeautifulSoup
import requests

url = 'http://example.com/'
response = requests.get(url)
soup = str(BeautifulSoup(response.text, 'html.parser'))
tree = html.fromstring(soup)
links = tree.xpath("//a/@href")
text_links = tree.xpath("//a/text()")
print('Ссылки из html: ', *links)
print('Названия ссылок из html: ', *text_links)
