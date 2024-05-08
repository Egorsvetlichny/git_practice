# You need to implement a function that takes as arguments a string consisting of letters
# and return a new string in which the repeated letters are replaced by the number of repetitions.

# Например: AAAABBCAA --> A4B2C1A2


def replace_repeat(string: str) -> str:
    counter = 1
    res = ''
    for i in range(1, len(string)):
        if string[i] == string[i - 1]:
            counter += 1
        else:
            res += f'{string[i - 1]}{counter}'
            counter = 1
    return res + f'{string[-1]}{counter}' if string else ''


def main():
    assert replace_repeat('AAAABBCAA') == 'A4B2C1A2'
    assert replace_repeat('AAAABBCAB') == 'A4B2C1A1B1'
    assert replace_repeat('ATAABBCAT') == 'A1T1A2B2C1A1T1'
    assert replace_repeat('TAABBCATT') == 'T1A2B2C1A1T2'
    assert replace_repeat('') == ''


if __name__ == '__main__':
    main()
