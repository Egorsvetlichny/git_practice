# Напишите программу, которая на основе данных таблицы создает список цитат из фильмов,
# выпущенных после 1995 года.


from bs4 import BeautifulSoup

import requests


def movie_quotes():
    url = 'https://ru.wikipedia.org/wiki/100_%D0%B8%D0%B7%D0%B2%D0%B5%D1%81%D1%82%D0%BD%D1%8B%D1%85_%D1%86%D0%B8%D1%82%D0%B0%D1%82_%D0%B8%D0%B7_%D0%B0%D0%BC%D0%B5%D1%80%D0%B8%D0%BA%D0%B0%D0%BD%D1%81%D0%BA%D0%B8%D1%85_%D1%84%D0%B8%D0%BB%D1%8C%D0%BC%D0%BE%D0%B2_%D0%B7%D0%B0_100_%D0%BB%D0%B5%D1%82_%D0%BF%D0%BE_%D0%B2%D0%B5%D1%80%D1%81%D0%B8%D0%B8_AFI'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    table = soup.find('table', 'wikitable')
    quotes = []

    for table_string in table.find_all('tr')[1:]:
        cells = table_string.find_all('td')
        if int(cells[6].get_text()) > 1995:
            quote = cells[1].get_text() + cells[2].get_text()
            quotes.append(quote.replace('\n', ' '))

    return quotes


def main():
    for quote in movie_quotes():
        print(quote)


if __name__ == '__main__':
    main()
