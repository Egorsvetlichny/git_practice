# Напишите регулярное выражения, которое находит в полученной от пользователя строке все слова с дефисом.

import re


def print_hyphenated_words(string: str) -> None:
    print(re.findall(r'\b\w+-\w+\b', string, re.I))


def main():
    print_hyphenated_words('Почему-то часто никак как-то получилось что-то зачем-то опять Кто-то')


if __name__ == '__main__':
    main()