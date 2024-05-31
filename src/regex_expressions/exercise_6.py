# Напишите программу, которая:
# - Получает от пользователя n строк с данными студентов.
# - Извлекает имена, фамилии и оценки по предметам (математика, физика, химия и биология соответственно)
# без использования методов строк и словарей.
# - Создает и выводит список словарей.

import re


def list_students_data(data: str) -> list:
    res = []
    pattern = re.compile(r'^(?P<Name>\w+),(?P<Lastname>\w+),(?P<Math>\d),(?P<Physics>\d),(?P<Chemistry>\d),'
                         r'(?P<Biology>\d)', re.M)
    for match in pattern.finditer(data):
        res.append(match.groupdict())

    return res


def main():
    students_data = """5
Денис,Ефремов,5,5,3,4
Юлия,Демидова,5,3,4,5
Евгения,Артемова,4,4,4,5
Сергей,Егоров,4,4,4,3
Кирилл,Антонов,4,5,3,3"""

    print(list_students_data(students_data))


if __name__ == '__main__':
    main()
