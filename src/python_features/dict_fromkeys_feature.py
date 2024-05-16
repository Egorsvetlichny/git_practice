# Класс dict имеет удобный метод fromkeys, который позволяет сформировать словарь с разными ключами и общим значением.
# Можно использовать dict comprehension.

keys = ['key1', 'key2', 'key3']

dict1 = {key: 'value' for key in keys}
dict2 = dict.fromkeys(keys, 'value')

assert dict1 == dict2
