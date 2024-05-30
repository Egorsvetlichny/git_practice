# Напишите регулярное выражение, которое меняет формат даты в URL с ГГГГ/ММ/ДД на ДД/ММ/ГГГГ в строке.

import re


def change_date_format(string: str) -> str:
    return re.sub(r'/(\d+)/(\d+)/(\d+)/', r'/\3/\2/\1/', string)


def main():
    print(change_date_format('https://www.washingtonpost.com/technology/2023/02/14/what-is-temu-super-bowl/'))


if __name__ == '__main__':
    main()
