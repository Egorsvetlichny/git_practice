# Write a function, which takes an input int and must return sum of digits in it.


def rec_sum_digits(number: int) -> int:
    if len(str(number)) == 1:
        return number
    return int(str(number)[0]) + rec_sum_digits(int(str(number)[1:]))


def main():
    assert rec_sum_digits(0) == 0
    assert rec_sum_digits(5) == 5
    assert rec_sum_digits(10) == 1
    assert rec_sum_digits(19) == 10
    assert rec_sum_digits(245) == 11
    assert rec_sum_digits(2394) == 18


if __name__ == '__main__':
    main()
