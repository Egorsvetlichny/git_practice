# Реализовать функцию, которая принимает и возвращает ту же строку, только где все символы сдвинуты на 13 символов,
# согласно порядковым номерам символов на клавиатуре.
# Также, необходимо учитывать регистр символов. Все остальные символы, кроме латинских букв, программа должна сдвигать
# без изменений.

def cezar13(string: str) -> str:
    result = ''

    for char in string:
        if (ord(char) >= ord('a') and ord(char) <= ord('m')) or (ord(char) >= ord('A') and ord(char) <= ord('M')):
            result += chr(ord(char) + 13)
        elif (ord(char) >= ord('n') and ord(char) <= ord('z')) or (ord(char) >= ord('N') and ord(char) <= ord('Z')):
            result += chr(ord(char) - 13)
        else:
            result += char

    return result


def main():
    assert cezar13('test') == 'grfg'
    assert cezar13('Test') == 'Grfg'
    assert cezar13('кTest  4я 1TEST3') == 'кGrfg  4я 1GRFG3'
    assert cezar13('') == ''


if __name__ == '__main__':
    main()
