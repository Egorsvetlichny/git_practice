# Напишите программу, которая составляет топ-20 языков программирования на основе рейтинга популярности TIOBE.

# Example format output: '1. Python: 14.83%'


from bs4 import BeautifulSoup
import requests


def parse_top_program_lang():
    url = 'https://www.tiobe.com/tiobe-index/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    soup = soup.find('tbody')
    prog_langs = soup.find_all('tr')

    res = []
    for prog_lang in prog_langs:
        prog_lang = prog_lang.find_all('td')
        # вычленяем название языка и его популярность в %
        res.append(f'{prog_lang[4].get_text()}: {prog_lang[5].get_text()}')
    # сортируем список по популярности языка
    res.sort(key=lambda x: float(x.split()[-1][:-1]), reverse=True)

    for i in range(20):
        print(f'{i + 1}. {res[i]}')
        i += 1


def main():
    parse_top_program_lang()


if __name__ == '__main__':
    main()
