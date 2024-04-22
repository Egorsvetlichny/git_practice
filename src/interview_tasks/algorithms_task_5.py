# Напишите функцию, которая принимает строку и увиличивает число в конце неё на единицу.
# Если числа в конце строки нет, то добавьте единицу к строке.

def add_one_to_number_in_str(string: str) -> str:
    letters = string.rstrip('0123456789')
    number = string[len(letters):]

    return letters + str(int(number) + 1).zfill(len(number)) if number else letters + '1'


def main():
    assert add_one_to_number_in_str('foo') == 'foo1'
    assert add_one_to_number_in_str('foobar23') == 'foobar24'
    assert add_one_to_number_in_str('foo0042') == 'foo0043'
    assert add_one_to_number_in_str('foo9') == 'foo10'
    assert add_one_to_number_in_str('foo099') == 'foo100'
    assert add_one_to_number_in_str('') == '1'
    assert add_one_to_number_in_str(' ') == ' 1'
    assert add_one_to_number_in_str('0999') == '1000'


if __name__ == '__main__':
    main()
