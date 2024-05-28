# Флаги - дополнительные параметры для Regex-шаблонов. Использовать можно и полную, и краткую форму параметра.

import re

# re.I, re.IGNORECASE – игнорирует регистр
string = 'Яблоко от яблони недалеко падает'
print(re.findall(r'ябл', string, re.I))
print()

# re.A, re.ASCII – находит ASCII-символы, игнорируя все остальные
string = 'одно из слов для обозначения дракона в японском - ドラゴン, doragon'
print(re.findall(r'\w+', string, re.A))
print()

# re.M, re.MULTILINE – находит совпадения в начале ^ и конце $ каждой строки в многострочном фрагменте текста
string = 'Это пример текста,\n состоящего из\n нескольких строк\n'
print(re.search(r'^\sсостоящего', string))
print(re.search(r'^\sсостоящего', string, re.M))
print()

# re.S, re.DOTALL – позволяет метасимволу "." возвращать совпадения по всем символам, включая \n
string = 'пример\n строки\n \nс \nсимволом "\n"'
print(re.findall(r'.', string))
print(re.findall(r'.', string, re.DOTALL))
print()

# re.X, re.VERBOSE – позволяет использовать комментарии в Regex-шаблонах
emails = ['python4ik@python.org', '@4##@%@mail.ru',
          'python@yandex.ru', 'my_em@il@mail.com']
pattern = re.compile(r'''
                     ^[a-zA-Z0-9_-]+ # первая часть адреса содержит буквы, цифры, подчеркивание и дефис
                     @ # первая часть адреса соединяется со второй символом @
                     [a-zA-Z.-]+$ # заключительная часть - доменное имя (может содержать дефис) и доменная зона
                     ''', re.X)
for email in emails:
    if re.fullmatch(pattern, email):
        print(email)
