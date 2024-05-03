# Write a function, which takes an input int n and must output all numbers from 1 to n.
# If n < 1 or n = 1, return n.


def rec_from_1_to_n(n: int) -> None:
    if n <= 1:
        print(n)
        return
    rec_from_1_to_n(n - 1)
    print(n)


def main():
    test_cases = [-5, 0, 1, 2, 5, 11]

    for i in range(len(test_cases)):
        print(f"Test {i + 1}: n = {test_cases[i]}")
        print("Output:")
        rec_from_1_to_n(test_cases[i])


if __name__ == '__main__':
    main()
