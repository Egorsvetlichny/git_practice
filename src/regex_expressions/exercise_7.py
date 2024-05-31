# Напишите регулярные выражения, которые:
# - Заменяют все вхождения слова «красный» на «зеленый», но только в том случае,
# если перед словом «красный» нет союза «и».
# - Находят все слова, которые не заканчиваются на «и» или «ый».
# - Находят все слова, которые не начинаются с букв «к», «ф», «о» и имеют длину 2 и более символов.

import re
from typing import Tuple


def check_change_string(string: str) -> Tuple[str, list, list]:
    res1 = re.sub(r'(?<!\bи\s)красный', r'зеленый', string)
    res2 = re.findall(r'\b\w+\b(?<![иый])', string)
    # res3 = re.findall(r'(?![кфо])(?=\w{2,})\b\w+\b', string, re.I)
    res3 = re.findall(r'(?![кфо])\b\w{2,}\b', string, re.I)

    return res1, res2, res3


def main():
    text = '''красноватый фиолетовый и красный 
красный и желтый красный желтый и красный
красный и оранжевый прекрасный окрас
розоватый и красный краснота'''

    [print(res, end='\n\n') for res in check_change_string(text)]


if __name__ == '__main__':
    main()
