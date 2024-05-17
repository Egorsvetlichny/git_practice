from collections import OrderedDict, ChainMap, Counter, defaultdict, deque, namedtuple

# OrderDict - словарь, применяющийся там, где важен порядок элементов. Например, для операций сравнения или хранение
# ключей в правильном порядке. Расплачиваемся памятью.
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 2, 'a': 1}

ordered_dict1 = OrderedDict(dict1)
ordered_dict2 = OrderedDict(dict2)

print("Словари равны:", dict1 == dict2)
print("Ориентированные словари равны:", ordered_dict1 == ordered_dict2)

print(ordered_dict1)
ordered_dict1.move_to_end('a')
print(ordered_dict1)
ordered_dict1.move_to_end('a', last=False)
print(ordered_dict1)

ordered_dict1['c'] = 3
ordered_dict1.popitem()
print(ordered_dict1)
ordered_dict1['c'] = 3
ordered_dict1.popitem(last=False)
print(ordered_dict1)
print()


# ChainMap - служит для логического объединения словарей (для поиска). Но через ChainMap меняется только первый словарь.
chain_map = ChainMap(dict1, {'d': 4, 'e': 5}, {'f': 6})
print(chain_map)
print('d' in chain_map)

chain_map['d'] = 10
print(chain_map)

print()


# Counter - служит для частотного анализа текста. Подсчитывает буквы в словах, слова или даже предложения в тексте.
# Работает только с hashable объектами.
counter = Counter('Hello, world and everyone!')
print(counter)
print(counter.most_common(1))

counter = Counter('Hello, world and everyone! World'.lower().split())
print(counter)
print(counter.most_common(3))

counter = Counter('Hello, world and everyone. I love my mom. The sun is so beautiful. I love my mom. '.split('. '))
print(counter)
print(counter.most_common(2))

print()


# defaultdict - Словарь со значениями по умолчанию.
# Значения по умолчанию подставляются при попытке обратиться к несуществующему ключу.
dict_int_default = defaultdict(int)
dict_int_default['a'] = 1
print(dict_int_default)
print(dict_int_default['a'])
print(dict_int_default['b'])
print(dict_int_default)

print('c' in dict_int_default)

dict_list_default = defaultdict(list, {'a': [1, 2, 3]})
print(dict_list_default['b'])
print(dict_list_default)

for key in 'hello, World and everyone! Hello, hello'.lower().split():
    dict_list_default[key].append(key)
print(dict_list_default)

print()


# deque - список, который быстро оперирует с обоими концами. Потокобезопасна. Принимает любой итерируемый объект
my_deque = deque([1, 2, 3, 4, 5], maxlen=3)
print(my_deque)

my_deque.appendleft(1)
print(my_deque)

print(my_deque.popleft())

my_deque.extendleft([1, 2])
print(my_deque)

print(1 in my_deque)

print()


# namedtuple - Именованный кортеж. Позволяет обращаться к элементам и по индексу, и по имени атрибута.
# Также не изменяем и быстр, как обычный кортеж. Похож на ООП.
Table = namedtuple('Table', 'shape color high weight price')
kitchen_table = Table('square', 'black', 140, 200, 23_999.99)
print(kitchen_table)
print(kitchen_table[0])
print(kitchen_table.color, kitchen_table.price)

hall_table = Table._make('circle, white, 130, 155, 10_500.00'.replace(',', '').split())
print(hall_table)
