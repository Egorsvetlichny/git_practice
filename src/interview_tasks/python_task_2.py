# Реализуйте функцию merge(), которая принимает два списка и возвращает словарь
# (ключ из первого списка, значение из второго), упорядоченный по ключам.
# Длина первого списка необязательно равна длине второго.

# Example
# Input: list1 = [4, 2, 5, 1], list2 = ['a', 'c', 'd', 'e', 'a', 'f']
# Output: {1: 'e', 2: 'c', 4: 'a', 5: 'd'}


def merge(list1: list, list2: list) -> dict:
    return dict(sorted(dict(zip(list1, list2)).items(), key=lambda x: x[0]))


def test():
    assert merge([4, 2, 5, 1], ['a', 'c', 'd', 'e', 'a', 'f']) == {1: 'e', 2: 'c', 4: 'a', 5: 'd'}
    assert merge([4, 2, 5, 7, 8, 9], ['a', 'c', 'd']) == {2: 'c', 4: 'a', 5: 'd'}
    assert merge([0], ['a']) == {0: 'a'}
    assert merge([], []) == {}


if __name__ == '__main__':
    test()
