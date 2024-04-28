# Напишите функцию, которая принимает список и возвращает число, встречающееся нечётное количество раз в списке.
# Во входном списке находится ровно одно число, которое встречается нечётное количество раз,
# либо такого числа нет вообще. В таком случае верните None

# Например: Input([1, 2, 2, 3, 3, 3, 4, 3, 3, 3, 2, 2, 1]), Output(4)


from typing import Union


def find_odd_number(arr: list) -> Union[None, int]:
    for item in arr:
        if arr.count(item) % 2 != 0:
            return item


def main():
    assert find_odd_number([1, 2, 2, 3, 3, 3, 4, 3, 3, 3, 2, 2, 1]) == 4
    assert find_odd_number([1, 2, 2, 2, 2, 2, 1, 2, 2]) == 2
    assert find_odd_number([1, 2, 2, 3, 3, 3, 4, 3, 3, 3, 2, 2, 1, 4]) is None
    assert find_odd_number([1]) == 1
    assert find_odd_number([]) is None


if __name__ == '__main__':
    main()
