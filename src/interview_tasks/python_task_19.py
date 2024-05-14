# Write a program that takes text and return two words: the most common and the longest word.
import collections
from typing import Tuple


# Example: "Kim loves his mother and his dad" --> 'his', 'mother'


def most_common_and_longest(string: str) -> Tuple[str, str]:
    # My solution:

    # most_common_word = longest_word = ''
    # max_word_counter = 0
    # for word in string.split():
    #     if len(word) > len(longest_word):
    #         longest_word = word
    #
    #     word_counter = string.count(word)
    #     if word_counter > max_word_counter:
    #         most_common_word = word
    #         max_word_counter = word_counter

    # -------------------------------------------------------

    # Optimal solution:

    if not string:
        return '', ''

    longest_word = max(string.split(), key=len)
    most_common_word, _ = collections.Counter(string.split()).most_common()[0]
    return most_common_word, longest_word


def main():
    assert most_common_and_longest('lorem ipsum dolor sis amet bobrkurva ti amo amet amet') == ('amet', 'bobrkurva')
    assert most_common_and_longest('') == ('', '')
    assert most_common_and_longest('lorem ipsum dolor sis amet ti amo') == ('lorem', 'lorem')
    assert most_common_and_longest('john') == ('john', 'john')
    assert most_common_and_longest('Kim loves his mother and his dad') == ('his', 'mother')


if __name__ == '__main__':
    main()
