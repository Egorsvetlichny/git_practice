# Write a function, which has an input string and must return a reverse string.


def rec_rev_string(string: str) -> str:
    if not string:
        return ''
    if len(string) == 1:
        return string[0]
    return string[-1] + string[-2::-1]


def main():
    assert rec_rev_string('') == ''
    assert rec_rev_string('a') == 'a'
    assert rec_rev_string('ab') == 'ba'
    assert rec_rev_string('Hello, world!') == '!dlrow ,olleH'
    assert rec_rev_string('Test TEST') == 'TSET tseT'


if __name__ == '__main__':
    main()
