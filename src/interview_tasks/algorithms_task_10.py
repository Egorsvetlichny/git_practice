# Реализовать функцию, получающую на вход целое положительное число, и возвращающую список, состоящий из двух рядом
# стоящих чисел последовательности Фибоначи, произведение которых наиболее близко к переданному в функцию числу.
# Также, в возвращаемом списке вернуть третьим элементом булево значение. True - если произведение чисел равно
# входному числу, False - если приближено, но не равно.

# Например: Input(4895), Output([55, 89, True])

def fib_search_times(number: int) -> list:
    a, b = 0, 1

    while a * b < number:
        a, b = b, a + b

    return [a, b, a * b == number]


def main():
    assert fib_search_times(4895) == [55, 89, True]
    assert fib_search_times(5895) == [89, 144, False]
    assert fib_search_times(0) == [0, 1, True]
    assert fib_search_times(1) == [1, 1, True]
    assert fib_search_times(2) == [1, 2, True]


if __name__ == '__main__':
    main()
