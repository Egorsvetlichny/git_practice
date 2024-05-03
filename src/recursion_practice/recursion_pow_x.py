# Write a function, which has an input int x and int y and must return x ** y.


def rec_fact(x: int, y: int) -> int:
    if y == 0:
        return 1
    if y == 1:
        return x
    return x * rec_fact(x, y - 1)


def main():
    assert rec_fact(0, 0) == 1
    assert rec_fact(100, 0) == 1
    assert rec_fact(0, 1) == 0
    assert rec_fact(200, 1) == 200
    assert rec_fact(2, 10) == 1024
    assert rec_fact(10, 4) == 10000
    assert rec_fact(5, 3) == 125


if __name__ == '__main__':
    main()
