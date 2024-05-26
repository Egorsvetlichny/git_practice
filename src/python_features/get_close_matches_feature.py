# В стандартной библиотеке difflib есть функция get_close_matches - этот метод ищет "наилучшие" возможные совпадения.
# Первый аргумент задаёт искомую строку, второй аргумент — список, в котором выполняется поиск.
# Также в метод можно передать необязательный аргумент n, который задаёт максимальное число возвращаемых совпадений.

from difflib import get_close_matches

some_list = ['puppy', 'appla', 'food', 'apple', 'peach', 'appel', 'ppale', 'aple']

similar = get_close_matches('apple', some_list)
print(similar)

similar = get_close_matches('apple', some_list, n=2)
print(similar)
