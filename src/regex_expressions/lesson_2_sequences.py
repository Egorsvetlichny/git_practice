# В регулярных выражениях знак "\" обозначает определенную последовательность символов.

import re

# Последовательности, которые используются для составления Regex-шаблонов:

# \A – проверяет, начинается ли строка с заданной последовательности символов или слов
string = 'О бойся Бармаглота, сын! Он так свирлеп и дик, А в глуще рымит исполин – Злопастный Брандашмыг.'
print(re.search(r'\AО бойся', string))
print()

# \b – проверяет, 1) начинается ли 2) заканчивается ли слово специфической последовательностью символов
string = 'www.mysite.com, www.yoursite.com, www.oursite.io, oursite.io.www'
print(re.findall(r'(www.)\b', string))
print(re.findall(r'(.io)\b', string))
print()

# \B – возвращает совпадение, если указанные символы присутствуют в строке, но 1) не в начале 2) не в конце слов
string = 'красный, зеленый, нытик'
print(re.findall(r'\Bк\B', string))
print(re.findall(r'\Bе\B', string))
print()

# \d – определяет, есть ли в строке цифры от 0 до 9
string = 'собеседование назначено на 12 мая'
print(re.findall(r'\d\d\d', string))
print(re.findall(r'\d\d', string))
print(re.findall(r'\d', string))
print()

# \D – соответствует всем символам, кроме цифр
string = '!#!@#@$%^номер начинается с +7'
print(re.findall(r'\D', string))
print()

# \s – соответствует одному пробелу
string = 'один пробел'
print(re.search(r'\s', string))
print(re.findall(r'\s\s', string))
print()

# \S – соответствует любому символу, кроме пробела
string = ' war r   i  or           '
print(re.findall(r'\S', string))
print()

# \w – соответствует любой букве, цифре или символу _
string1, string2 = '!@$^^$%&*()@', 's5tf7_  '
print(re.findall(r'\w', string1))
print(re.findall(r'\w', string2))
print()

# \W – совпадает с любым специальным символом, игнорирует буквы, цифры и _
string1, string2 = '!@~#$%^&*(', 'a28df_r4ghgh'
print(re.findall(r'\W', string1))
print(re.findall(r'\W', string2))
print()

# \Z – проверяет, заканчивается ли строка нужной последовательностью
string1, string2 = 'самый популярный язык - Python', 'главный язык интернета - JavaScript'
print(re.search(r'Script\Z', string2))
print(re.search(r'Java\Z', string1))
print()
