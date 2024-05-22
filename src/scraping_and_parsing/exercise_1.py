# Напишите программу для получения названий последних статей из блога издательства O’Reilly


from bs4 import BeautifulSoup
import requests


def get_titles_oreilly():
    url = 'https://www.oreilly.com/radar/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    titles = soup.find_all('h2', 'post-title')

    return titles


def main():
    for title in get_titles_oreilly():
        print(title.get_text())


if __name__ == '__main__':
    main()
