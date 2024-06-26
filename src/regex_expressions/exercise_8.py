# Напишите регулярные выражения, которые:
# - Удаляют все html-теги из полученного от пользователя текста.
# - Вставляют пробелы перед заглавными буквами в тексте и ставят точки в конце предложений.

import re


def change_string(string: str) -> str:
    string = re.sub(r'</?\w+>', r'', string)  # Удаляем теги html
    string = re.sub(r'(?<!^)([А-ЯA-Z])', r'. \1', string, flags=re.M)  # Добавляем точки и пробелы между предложениями
    return re.sub(r'(?<=.)$', r'.', string, flags=re.M)  # Добавляем точки в конце строк


def main():
    text = """<h1>Это заголовок первого уровня</h1><p>Это текст параграфа<strong>
Это важный текст внутри параграфа</strong></p>\n
<p>Это второй параграф</p>\n
<h1>Это заголовок первого уровня</h1>\n<p>Это текст параграфа<strong>Это важный текст внутри параграфа</strong></p>
<p>Это второй параграф</p>
"""

    print(change_string(text))


if __name__ == '__main__':
    main()
