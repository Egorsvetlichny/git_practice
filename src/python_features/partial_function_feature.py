# Функция partial из библиотеки functools - это такая функция, которая принимает другую функцию
# с несколькими параметрами и возвращает функцию, но уже с меньшим количеством параметров.

from functools import partial


def greet_person(greet_word, name, separator, emphasis):
    print(f'{greet_word}{separator} {name}{emphasis}')


if __name__ == '__main__':
    new_greet_func = partial(greet_person, greet_word='Hello', separator=',', emphasis='!')

    new_greet_func(name='world')
    new_greet_func(name='Egor')
    new_greet_func(name='everyone')
