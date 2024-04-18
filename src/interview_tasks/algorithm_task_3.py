# На вход подаётся целое число. Вернуть количество нулей в конце факториала этого числа.

# Например, на входе в функцию число 20 -- на выходе 4.


def count_zeros(n: int) -> int:
    count_of_zeros = 0
    while n:
        n = n // 5
        count_of_zeros += n

    return count_of_zeros


def main():
    assert count_zeros(6) == 1
    assert count_zeros(10) == 2
    assert count_zeros(17) == 3
    assert count_zeros(0) == 0
    assert count_zeros(1) == 0
    assert count_zeros(44) == 9


if __name__ == '__main__':
    main()
