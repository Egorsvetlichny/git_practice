# Given a natural number n>1. Output all prime multipliers of this number in the order of non-decreasing multiplicity.
# The algorithm must have complexity O(log n)


def rec_multipliers(n: int, m: int = 2) -> None:
    if m > n / 2:
        print(int(n))
        return
    if n % m == 0:
        print(m)
        rec_multipliers(n / m, m)
    else:
        rec_multipliers(n, m + 1)


def main():
    test_cases = [0, 1, 2, 3, 4, 5, 10, 13, 27, 144, 22]

    for i in range(len(test_cases)):
        print(f"Test {i + 1}: n = {test_cases[i]}")
        print("Output:")
        rec_multipliers(test_cases[i])


if __name__ == '__main__':
    main()
