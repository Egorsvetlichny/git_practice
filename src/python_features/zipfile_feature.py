# zipfile - встроенный модуль для работы с архивами zip.

from zipfile import ZipFile


def main():
    file_name = 'test.zip'

    with ZipFile(file_name, 'r') as zf:
        zf.printdir()  # Выводит содержимое архива в виде списка строк.
        zf.extractall()  # Извлекает все файлы из архива.


if __name__ == '__main__':
    main()
