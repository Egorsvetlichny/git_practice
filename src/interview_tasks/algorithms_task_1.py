# Реализуйте функцию count_zeros(), которая принимает квадратную матрицу, состоящую из нулей и единиц,
# элементы которой в каждой строке и столбце отсортированы в порядке неубывания,
# и возвращает общее количество нулей в матрице.


from typing import List


def count_zeros(matrix: List[List[int]]) -> int:
    if len(matrix) == 0 or len(matrix[0]) == 0:
        return 0

    i, j = 0, len(matrix) - 1
    sum_zeros = 0

    while i <= len(matrix) - 1 and j >= 0:
        if matrix[i][j] == 0:
            sum_zeros += j + 1
            i += 1
        else:
            j -= 1

    return sum_zeros


def test():
    mtrx = [[0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1],
            [0, 0, 1, 1, 1],
            [0, 0, 1, 1, 1],
            [1, 1, 1, 1, 1]]

    assert count_zeros(mtrx) == 13

    mtrx = [[0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0]]

    assert count_zeros(mtrx) == 25

    mtrx = [[1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1]]

    assert count_zeros(mtrx) == 0

    mtrx = [[]]

    assert count_zeros(mtrx) == 0

    mtrx = [[0, 1],
            [0, 1]]

    assert count_zeros(mtrx) == 2


if __name__ == '__main__':
    test()
