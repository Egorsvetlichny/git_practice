# Напишите программу для скачивания полноразмерных обложек из профилей книг на LiveLib.
# Обложки открываются после двойного клика по миниатюре.


from bs4 import BeautifulSoup
import requests


def parse_book_cover():
    url = 'https://www.livelib.ru/book/1002978643-ohotnik-za-tenyu-donato-karrizi'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Выделяем содержимое аттрибута onclick
    book_cover = soup.find('div', 'bc-menu__image-wrapper')['onclick']
    # Получаем url в кавычках
    book_cover_url = book_cover.replace(',', '').split()[1]

    response = requests.get(book_cover_url[1:-1])
    if response.status_code == 200:
        # Парсим url на название книги и расширение
        file_name = response.url.split('/')[-1].split('__')[-1]
        # Создаём изображение с указанным именем
        with open(file_name, 'wb') as file:
            file.write(response.content)


def main():
    parse_book_cover()


if __name__ == '__main__':
    main()
