# Написать функцию, принимающую 3 целых числа (RGB) и приводящие их к шестнадцатеричному коду.
# Если значения не в диапазоне 0-255, то округлить их до ближайших допустимых значений

# Например: Input(255, 255, 255), Output('FFFFFF')


def rgb_int_to_hex(r: int, g: int, b: int) -> str:
    rgb = [r, g, b]
    res = ''

    for color in rgb:
        if color >= 255:
            res += 'FF'
        elif color <= 0:
            res += '00'
        else:
            if len(hex(color)[2:]) == 2:
                res += hex(color)[2:].upper()
            else:
                res += '0' + hex(color)[2:].upper()

    return res


def main():
    assert rgb_int_to_hex(255, 255, 255) == 'FFFFFF'
    assert rgb_int_to_hex(255, 255, 310) == 'FFFFFF'
    assert rgb_int_to_hex(0, 0, 0) == '000000'
    assert rgb_int_to_hex(148, 0, 211) == '9400D3'
    assert rgb_int_to_hex(-234, 0, 4235) == '0000FF'


if __name__ == '__main__':
    main()
