# Write a program that takes a number as input and decomposes it into prime factors.
# Return the prime factors as a list.

# Example: "20" --> [2, 2, 5]


def prime_factors(number: int) -> list:
    i = 2
    res = []
    while i <= number // 2:
        if number % i == 0:
            number /= i
            res.append(i)
        else:
            i += 1
    res.append(number)
    return res


def main():
    assert prime_factors(20) == [2, 2, 5]
    assert prime_factors(0) == [0]
    assert prime_factors(13) == [13]
    assert prime_factors(120) == [2, 2, 2, 3, 5]
    assert prime_factors(1000) == [2, 2, 2, 5, 5, 5]
    assert prime_factors(17) == [17]


if __name__ == '__main__':
    main()
