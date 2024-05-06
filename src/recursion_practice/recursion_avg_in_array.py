# Given an array of int numbers. Return avg value of this array.


def rec_avg_value_in_list(arr: list, i: int = 0, summ: int = 0) -> float:
    if not arr:
        return 0
    if i == len(arr):
        return summ / i
    return rec_avg_value_in_list(arr, i + 1, summ + arr[i])


def main():
    assert rec_avg_value_in_list([]) == 0
    assert rec_avg_value_in_list([1]) == 1
    assert rec_avg_value_in_list([0, 0]) == 0
    assert rec_avg_value_in_list([1, 2]) == 1.5
    assert rec_avg_value_in_list([1, 2, 3]) == 2
    assert rec_avg_value_in_list([5, 4, 1, 0, 2, 0]) == 2
    assert rec_avg_value_in_list([2, 1024]) == 513


if __name__ == '__main__':
    main()
