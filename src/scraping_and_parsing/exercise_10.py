# Напишите программу для получения главных новостей (на русском) с портала Habr.
# Каждый заголовок должен сопровождаться ссылкой на полный текст новости.

# Example format output: 'Honda запатентовала съёмные подушки безопасности для мотоциклистов
#                         https://habr.com/ru/news/t/721142/'


from bs4 import BeautifulSoup
import requests


def parse_habr_news():
    url = 'https://habr.com/ru/news/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    articles = soup.find_all('a', 'tm-title__link')
    [print(f"{article.get_text()}\nhttps://habr.com{article['href']}\n") for article in articles]


def main():
    parse_habr_news()


if __name__ == '__main__':
    main()
