# Write a function, which takes an input str word and return True if a word is a palindrom or False if it isn't


def rec_check_palindrom(word: str) -> bool:
    if not word:
        return True
    if len(word) == 1:
        return True
    if word[0].lower() == word[-1].lower():
        if len(word) == 2:
            return True
        return rec_check_palindrom(word[1:-1])
    else:
        return False


def main():
    assert rec_check_palindrom('') is True
    assert rec_check_palindrom('t') is True
    assert rec_check_palindrom('tT') is True
    assert rec_check_palindrom('Tnt') is True
    assert rec_check_palindrom('test') is False
    assert rec_check_palindrom('Madam') is True
    assert rec_check_palindrom('AbraCadabraarbadacarba') is True


if __name__ == '__main__':
    main()
