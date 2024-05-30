# Напишите регулярное выражение, которое удаляет из текста все знаки препинания, кроме дефиса.

import re


def delete_punctuation(string: str) -> str:
    return re.sub(r'[!?:;\.,"\']', '', string)


def main():
    print(delete_punctuation('"Это" - фрагмент текста, для обработки?!.. '))


if __name__ == '__main__':
    main()
