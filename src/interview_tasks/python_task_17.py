# Write a program that checks that a number is perfect.
# A perfect number is a natural number equal to the sum of all its eigenvalues.

# Example: "28" --> True (1 + 2 + 4 + 7 + 14 = 28)


def get_dividers(number: int) -> list:
    res = []
    for i in range(1, number // 2 + 1):
        if number % i == 0:
            res.append(i)
    return res


def perfect_number(number: int) -> bool:
    return True if number == sum(get_dividers(number=number)) else False


def main():
    assert perfect_number(28) is True
    assert perfect_number(27) is False
    assert perfect_number(6) is True
    assert perfect_number(496) is True
    assert perfect_number(8128) is True


if __name__ == '__main__':
    main()
