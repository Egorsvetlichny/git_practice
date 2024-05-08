# Write a function to count the vowels in a string

# Например: "Привет, мир!" --> 3


def vowels_counter(string: str) -> int:
    counter_vowels = 0

    # Not optimal decision
    # for letter in 'аеёиоуыэюяeyuioa':
    #     counter_vowels += string.lower().count(letter)

    for letter in string.lower():
        if letter in 'аеёиоуыэюяeyuioa':
            counter_vowels += 1
    return counter_vowels


def main():
    assert vowels_counter("Привет, мир!") == 3
    assert vowels_counter("") == 0
    assert vowels_counter("Hello, world") == 3
    assert vowels_counter("My name is Egor") == 6
    assert vowels_counter("YyYяяЯ") == 6


if __name__ == '__main__':
    main()
