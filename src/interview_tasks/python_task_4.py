# You get an array of numbers, return the sum of all the positives ones

def positive_sum(arr: list) -> int:
    return sum(item for item in arr if item > 0)


def main():
    assert positive_sum([0, 2, 1, -4, 2, -6, 3, 5, 0, -3]) == 13
    assert positive_sum([]) == 0
    assert positive_sum([5]) == 5
    assert positive_sum([-5]) == 0


if __name__ == '__main__':
    main()
