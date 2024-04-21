# Напишите функцию, которая принимает строку и возвращает первый символ, который нигде в строке не повторяется.
# Функция должна возвращать исходный регистр символа.

def first_nonrepeat_char(string: str) -> str:
    for i in string:
        if string.lower().count(i.lower()) == 1:
            return i

    return ''


def main():
    assert first_nonrepeat_char('sTReSS') == 'T'
    assert first_nonrepeat_char('') == ''
    assert first_nonrepeat_char(' ') == ' '
    assert first_nonrepeat_char('mama is the best') == 'i'
    assert first_nonrepeat_char('I love my dad') == 'I'
    assert first_nonrepeat_char(' very_good') == ' '


if __name__ == '__main__':
    main()
