# Напишите функцию, которая принимает строку и возвращает эту сторку, переворачивая все слова более 5 букв в ней.
# Во входной строке располагаются только слова и пробелы.

# Например: Input('Hey fellow warriors'), Output('Hey wollef sroirraw')


def change_string(string: str) -> str:
    return ' '.join([word if len(word) <= 5 else word[::-1] for word in string.split()])


def main():
    assert change_string('Hey fellow warriors') == 'Hey wollef sroirraw'
    assert change_string('This is a test') == 'This is a test'
    assert change_string('This is another test') == 'This is rehtona test'
    assert change_string('') == ''
    assert change_string('abracadabra') == 'arbadacarba'


if __name__ == '__main__':
    main()
