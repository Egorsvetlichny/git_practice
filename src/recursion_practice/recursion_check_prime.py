# Given a natural number greater than 1. Check whether it is prime.
# The program should return 'YES' if the number is prime and 'NO' if the number is composite.


def rec_check_prime(number: int, k=2) -> str:
    if k > number / 2:
        return 'YES'
    if number % k == 0:
        return 'NO'
    else:
        return rec_check_prime(number, k + 1)


def main():
    assert rec_check_prime(2) == 'YES'
    assert rec_check_prime(3) == 'YES'
    assert rec_check_prime(4) == 'NO'
    assert rec_check_prime(144) == 'NO'
    assert rec_check_prime(13) == 'YES'
    assert rec_check_prime(1500) == 'NO'


if __name__ == '__main__':
    main()
