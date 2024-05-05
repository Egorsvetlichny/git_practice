# Given a number n whose decimal notation does not contain zeros.
# Get the number written with the same digits but in the opposite order.
# The function must return an integer number, which is the result of the program,
# you cannot output the number one digit at a time.


def rec_reverse_number(n: int, i=0) -> int:
    if len(str(n)) == 0:
        return 0
    return (i * 10 + int(str(n)[0])) + rec_reverse_number(int(str(n)[1:]), i + 1)


def main():
    assert rec_reverse_number(1) == 1
    assert rec_reverse_number(7) == 7
    assert rec_reverse_number(12) == 21
    assert rec_reverse_number(145) == 541
    assert rec_reverse_number(1719) == 9171


if __name__ == '__main__':
    main()
