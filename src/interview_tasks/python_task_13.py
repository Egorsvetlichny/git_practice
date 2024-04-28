# Напишите функцию, которая принимает число и возвращает сумму его цифр.
# Если сумма цифр не однозначное число, тогда цифры складываются ещё, пока она не станет одной цифрой.

# Например: Input(942), Output(6)


def find_odd_number(number: int) -> int:
    if len(str(number)) == 1:
        return number
    else:
        return find_odd_number(sum(int(i) for i in str(number)))


def main():
    assert find_odd_number(942) == 6
    assert find_odd_number(9) == 9
    assert find_odd_number(0) == 0
    assert find_odd_number(19) == 1
    assert find_odd_number(99999999999992) == 2


if __name__ == '__main__':
    main()
