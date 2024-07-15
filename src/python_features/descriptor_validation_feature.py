# Дескрипторы часто используются в качестве валидаторов атрибутов.
# Они позволяют проверить, что значения атрибутов корректны.

class BookStrAttribute:
    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __set__(self, instance, value):  # Валидация атрибута
        if not isinstance(value, str):
            raise TypeError(f'Значение атрибута {self.name} должно быть строкой')
        setattr(instance, self.name, value)

    def __get__(self, instance, owner):
        return getattr(instance, self.name, None)


class Book:
    title = BookStrAttribute()
    author = BookStrAttribute()

    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f'"{self.title}" by {self.author}'


def main():
    assert str(Book("The Hobby", "John Doe")) == '"The Hobby" by John Doe'

    try:
        Book("Преступление и наказание", 234)  # Некорректный тип аргумента
        Book((1, 'beef', {1, 2, 3}, {'1': 1, '2': 2, '3': 3}), 'А.С. Пушкин')  # Некорректный тип аргумента
    except TypeError:
        assert True
    else:
        assert False


if __name__ == '__main__':
    main()
