# You get an integer number, return this number negative

def make_negative(number: int) -> int:
    return number if number <= 0 else number * -1


def main():
    assert make_negative(5) == -5
    assert make_negative(-5) == -5
    assert make_negative(0) == 0
    assert make_negative(1234) == -1234


if __name__ == '__main__':
    main()
