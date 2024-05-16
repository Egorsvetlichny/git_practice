# Функция total_ordering из модуля functools позволяет реализовать под капотом методы  lt, le, gt, ge.
# Для обеспечения работы функции нужно лишь реализовать методы __lt__ и __eq__.

from functools import total_ordering


@total_ordering
class Value:
    def __init__(self, value):
        self.value = value

    def __lt__(self, other):
        return self.value < other.value

    def __eq__(self, other):
        return self.value == other.value


if __name__ == '__main__':
    value_100 = Value(100)
    value_75 = Value(75)

    # Все assert'ы отработают без ошибок
    assert value_100 != value_75
    assert value_100 > value_75
    assert value_75 < value_100
    assert value_100 >= value_75
    assert value_75 <= value_100
    assert (value_100 == value_75) is False
