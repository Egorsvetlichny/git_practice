# Write a program that will convert a decimal number into a binary number.

# Example: "17" --> 10001


def from_dec_to_bin(number: int) -> int:
    res = ''
    while number >= 2:
        res += str(number % 2)
        number //= 2
    if number % 2 != 0:
        res += '1'
    return int(res[::-1])


def main():
    assert from_dec_to_bin(17) == 10001
    assert from_dec_to_bin(32) == 100000
    assert from_dec_to_bin(1024) == 10000000000
    assert from_dec_to_bin(113) == 1110001


if __name__ == '__main__':
    main()
