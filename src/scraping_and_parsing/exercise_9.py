# Напишите программу, которая сохраняет в текстовый файл данные о фэнтези фильмах с 10 первых страниц
# соответствующего раздела IMDb. Если у фильма/сериала еще нет рейтинга, следует указать N/A.
# Ожидаемый результат в файле fantasy_movies.txt – 500 записей

# Example format output: 'Мандалорец, (2019– ), 8.7'


from bs4 import BeautifulSoup
import mechanicalsoup


def parse_fantasy_movies():
    url = 'https://www.imdb.com/search/title/?genres=fantasy'
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 "
                      "Safari/537.36", "Accept-Language": "ru-RU"}

    browser = mechanicalsoup.Browser()

    for _ in range(10):
        response = browser.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        more_button = soup.find("a", "lister-page-next button")

        titles_soup = soup.find_all('h3', 'ipc-title__text')
        # Список с заголовками фильмов
        titles = [t.get_text().split(maxsplit=1)[-1] for t in titles_soup[:-1]]

        soup = soup.find_all('li', 'ipc-metadata-list-summary-item')

        # Список с годами фильмов
        years = [year.find('span', 'dli-title-metadata-item').text.strip() for year in soup if year]

        # Список с рейтингом фильмов
        rates = []
        for rating in soup:
            rating = rating.find('span', 'ratingGroup--imdb-rating')
            rates.append(rating.text.split('\xa0')[0]) if rating else rates.append('N/A')

        with open('fantasy_movies.txt', 'a', encoding='utf-8') as file:
            for title, year, rating in zip(titles, years, rates):
                file.write(f'{title}, ({year}), {rating}\n')

        if more_button:
            url = more_button['href']


def main():
    parse_fantasy_movies()


if __name__ == '__main__':
    main()
