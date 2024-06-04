# Функция cycle() из itertools принимает на вход итерируемый объект и создает бесконечный итератор,
# циклически возвращающий элементы данного объекта.
# Когда элементы последовательности заканчиваются, итерация начинается вновь с первого элемента.

# Функция islice() - возвращает итератор по подмножеству переданного объекта.


from itertools import cycle, islice


def main():
    items = [1, 3, 4, 63]
    # for item in cycle(items):
    #     print(item)

    for item in islice(cycle(items), 2, 10):
        print(item)


if __name__ == '__main__':
    main()
