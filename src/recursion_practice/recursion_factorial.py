# Write a function, which has an input int and must return its factorial.


def rec_fact(number: int) -> int:
    if number == 0:
        return 1
    if number == 1:
        return 1
    return number * rec_fact(number - 1)


def main():
    assert rec_fact(0) == 1
    assert rec_fact(1) == 1
    assert rec_fact(2) == 2
    assert rec_fact(3) == 6
    assert rec_fact(6) == 2 * 3 * 4 * 5 * 6


if __name__ == '__main__':
    main()
