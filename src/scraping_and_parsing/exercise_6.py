# Напишите программу, которая составляет рейтинг топ-100 лучших триллеров на основе этого списка.

# Example format output: '1. "Побег из Шоушенка", Стивен Кинг - 4.6'


from bs4 import BeautifulSoup
import requests


def parse_top_rating_films():
    url = 'https://www.livelib.ru/genre/%D0%A2%D1%80%D0%B8%D0%BB%D0%BB%D0%B5%D1%80%D1%8B/top'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    films = soup.find('ul', 'lists__list')
    titles = films.find_all('a', 'book-item__title')
    authors = films.find_all('a', 'book-item__author')
    rating = [f.get_text().replace(',', '.') for f in films.find_all('div', 'book-item__rating')]

    res = []
    for title, author, rating in zip(titles, authors, rating):
        res.append(f'"{title.get_text()}", {author.get_text()} - {rating}')

    res.sort(key=lambda x: float(x.split()[-1]), reverse=True)

    for i in range(len(res)):
        print(f'{i + 1}. {res[i]}')


def main():
    parse_top_rating_films()


if __name__ == '__main__':
    main()
