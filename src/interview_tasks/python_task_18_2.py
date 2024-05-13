# Write a program that will convert a binary number into a decimal number.

# Example: "10001" --> 17


def from_bin_to_dec(number: int) -> int:
    number = ''.join(reversed(str(number)))
    return sum([2 ** i for i in range(len(number)) if number[i] == '1'])


def main():
    assert from_bin_to_dec(10001) == 17
    assert from_bin_to_dec(100000) == 32
    assert from_bin_to_dec(10000000000) == 1024
    assert from_bin_to_dec(1110001) == 113


if __name__ == '__main__':
    main()
