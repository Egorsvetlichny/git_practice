# Write a function, which return a sum of elements in list.


def rec_sum(arr: list) -> int:
    if not arr:
        return 0
    if len(arr) == 1:
        return arr[0]
    return arr.pop() + rec_sum(arr)


def main():
    assert rec_sum([]) == 0
    assert rec_sum([5]) == 5
    assert rec_sum([1, 6]) == 7
    assert rec_sum([1, 6, 2]) == 9
    assert rec_sum([1, 6, 2, 5, 6, 2]) == 22


if __name__ == '__main__':
    main()
