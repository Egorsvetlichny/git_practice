# Дан массив из целых чисел, среди которых есть нуль.
# Нужно сделать так, чтобы на входе функция получала массив,
# а в конце выводила этот массив с нулями в конце.

def add_zeros_to_end(arr: list) -> list:
    # zero_counter = 0
    # i = 0
    #
    # while i < len(arr):
    #     if arr[i] == 0:
    #         zero_counter += 1
    #         arr.pop(i)
    #     else:
    #         i += 1
    #
    # arr.extend([0 for _ in range(zero_counter)])

    return sorted(arr, key=lambda x: x == 0)


def main():
    assert add_zeros_to_end([1, 3, 0, 0, 1, 2, 0, 9, 1]) == [1, 3, 1, 2, 9, 1, 0, 0, 0]
    assert add_zeros_to_end([0, 5, 0, 0, 1, 0, 0, 9, 0]) == [5, 1, 9, 0, 0, 0, 0, 0, 0]
    assert add_zeros_to_end([]) == []
    assert add_zeros_to_end([0, 0, 0]) == [0, 0, 0]
    assert add_zeros_to_end([0]) == [0]


if __name__ == '__main__':
    main()
