# Способы объединения словарей

dict1 = {'one': 1, 'two': 2}
dict2 = {'three': 3, 'four': 4}

print({**dict1, **dict2})
print(dict1 | dict2)
# print(dict1 |= dict2) в последнем обновлении
