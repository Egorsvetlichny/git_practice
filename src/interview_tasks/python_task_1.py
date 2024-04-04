# Реализуйте функцию convert(), которая принимает числовое значение n,
# и возвращает строку вида '01234567891011...n'

def convert(n: int) -> str:
    return ''.join(map(str, range(n + 1)))


def test():
    assert convert(5) == '012345'
    assert convert(10) == '012345678910'
    assert convert(0) == '0'
    assert convert(1) == '01'


if __name__ == '__main__':
    test()