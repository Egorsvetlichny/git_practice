# You get an integer number, return this number opposite

def make_opposite(number: int) -> int:
    return number * (-1)


def main():
    assert make_opposite(10) == -10
    assert make_opposite(-10) == 10
    assert make_opposite(0) == 0


if __name__ == '__main__':
    main()
