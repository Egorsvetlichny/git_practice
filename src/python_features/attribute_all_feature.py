# С помощью атрибута __all__ можно ограничить экспорт объектов из модуля. По умолчанию экспортируются все.

def foo():
    print('foo')


def bar():
    print('bar')


def say_hello_world():
    print('Hello, world!')


# Ограничиваем экспорт. Функция 'foo' экспортироваться в другие модули не будет
__all__ = ['bar', 'say_hello_world']
