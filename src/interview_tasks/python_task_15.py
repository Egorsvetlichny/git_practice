# Write a program that checks whether a number is an Armstrong number.
# An Armstrong number is a natural number which, in a given number system,
# is equal to the sum of its digits raised to a power equal to the number of its digits.

# For example: "371" --> True (3**3 + 7**3 + 1**3 = 371)


def if_armstrong(number: int) -> bool:
    if number == sum([int(i) ** len(str(number)) for i in str(number)]):
        return True
    return False


def main():
    assert if_armstrong(371) is True
    assert if_armstrong(255) is False
    assert if_armstrong(1) is True
    assert if_armstrong(0) is True
    assert if_armstrong(33) is False
    assert if_armstrong(1634) is True
    assert if_armstrong(153) is True


if __name__ == '__main__':
    main()
