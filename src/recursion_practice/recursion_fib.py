# Write a function, which takes an input int "i" and must return fib number on "i" position.
# Positions starts with 1, NOT 0!
from typing import Union


def rec_fib(i: int) -> Union[int, str]:
    if i < 1:
        return 'Incorrect input, i must be greater than 0!'
    if i == 1:
        return 1
    if i == 2:
        return 1
    return rec_fib(i - 1) + rec_fib(i - 2)


def main():
    assert rec_fib(1) == 1
    assert rec_fib(2) == 1
    assert rec_fib(3) == 2
    assert rec_fib(4) == 3
    assert rec_fib(5) == 5
    assert rec_fib(11) == 89
    assert rec_fib(-4) == 'Incorrect input, i must be greater than 0!'
    assert rec_fib(0) == 'Incorrect input, i must be greater than 0!'


if __name__ == '__main__':
    main()
