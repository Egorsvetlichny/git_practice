# Напишите программу, которая с помощью Regex-шаблона определяет,
# сколько слов в полученной от пользователя строке начинаются с «ко» или «коо».

import re


def count_right_words(string: str) -> None:
    print(len(re.findall(r'\bкоо*\w+\b', string, re.I)))


def main():
    count_right_words('Книга, компьютер крот, Колобок колхоз кооперация. ноутбук карандаш, координатор')


if __name__ == '__main__':
    main()
