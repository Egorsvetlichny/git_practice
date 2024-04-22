# Дан массив с целыми числами. Задача, упорядочить массив по возрастанию суммы цифр в числах.


def sum_digits(arr: list) -> list:
    return sorted(arr, key=lambda x: sum(int(i) for i in str(x)))


def main():
    assert sum_digits([103, 123, 4444, 99, 2000]) == [2000, 103, 123, 4444, 99]
    assert sum_digits([]) == []
    assert sum_digits([123]) == [123]
    assert sum_digits([0]) == [0]


if __name__ == '__main__':
    main()
