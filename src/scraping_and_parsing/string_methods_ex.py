from bs4 import BeautifulSoup
import requests

url = 'http://example.com/'
response = requests.get(url)
soup = str(BeautifulSoup(response.text, 'html.parser'))
start = soup.find('href="') + 6
end = soup.find('">More')
link = soup[start:end]
print(link)
