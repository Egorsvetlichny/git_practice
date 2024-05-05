# Given a monotone sequence in which each natural number k occurs exactly k times:
# 1, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 4,...
# Given a natural number n, return string which contains the first n members of this sequence.


def rec_triangular_seq(n: int) -> str:
    summ = digit = 0
    if n == 0:
        return ''
    if n == 1:
        return '1'
    else:
        for i in range(1, n + 1):
            summ += i
            if summ >= n:
                digit = i
                break
        return rec_triangular_seq(n - 1) + ', ' + str(digit)


def main():
    test_cases = [5, 0, 1, 2, 10]

    for i in range(len(test_cases)):
        print(f"Test {i + 1}: n = {test_cases[i]}")
        print("Output:")
        print(rec_triangular_seq(test_cases[i]))


if __name__ == '__main__':
    main()
