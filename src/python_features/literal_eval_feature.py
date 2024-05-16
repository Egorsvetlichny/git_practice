# Функция literal_eval из модуля ast поможет распарсить строку на пайтоновские типы данных.

from ast import literal_eval

response = "{'a': [1, 3, 52, 0], 'b': {'a1': 23, 'a2': 7}, 'c': {2, 3, 2, 1, 1, 2}, 'd': ('box', 25)}"

print(literal_eval(response))

assert isinstance(literal_eval(response), dict)
assert isinstance(literal_eval(response)['a'], list)
assert isinstance(literal_eval(response)['b'], dict)
assert isinstance(literal_eval(response)['c'], set)
assert isinstance(literal_eval(response)['d'], tuple)
