# Напишите программу для получения рейтинга 250 лучших фильмов по версии IMDb. Названия должны быть на русском языке.

# Example format output: '1. Побег из Шоушенка, (1994), 9.3'


from bs4 import BeautifulSoup
import requests


def parse_top_250_movies():
    url = 'https://www.imdb.com/chart/top/'
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 "
                      "Safari/537.36",
        "Accept-Language": "ru-RU"}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    titles = soup.find_all('h3', 'ipc-title__text')[1:251]
    years = soup.find_all('div', 'sc-b189961a-7 feoqjK cli-title-metadata')[0:250]
    rating = soup.find_all('span',
                           'ipc-rating-star ipc-rating-star--base ipc-rating-star--imdb ratingGroup--imdb-rating')[
             0:250]

    for t, y, r in zip(titles, years, rating):
        print(f'{t.get_text()}, ({y.get_text()[:4]}), {r.get_text().split()[0]}')


def main():
    parse_top_250_movies()


if __name__ == '__main__':
    main()
