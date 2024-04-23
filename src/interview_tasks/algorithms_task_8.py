# Найти максимальную сумму непрерывной подпоследовательности в списке целых чисел.
# Если список состоит только из отрицательных чисел, верните 0.

def sum_subsequence(arr: list) -> int:
    max_sum = summ = 0
    for item in arr:
        summ += item
        max_sum = max(max_sum, summ)

        if summ < 0: summ = 0

    return max_sum


def main():
    assert sum_subsequence([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
    assert sum_subsequence([]) == 0
    assert sum_subsequence([-4, -5, -4, -10, -1, -1]) == 0
    assert sum_subsequence([-4, -5, -4, 10, -1, -1]) == 10


if __name__ == '__main__':
    main()
