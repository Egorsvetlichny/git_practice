# Написать реализацию функций принимающих друг друга и реализующих калькулятор.

# Например:
# seven(times(five()))  must return 35
# four(plus(nine()))  must return 13
# eight(minus(three()))  must return 5
# six(divided_by(two()))  must return 3


def zero(func=None): return int(func(0)) if func else 0
def one(func=None): return int(func(1)) if func else 1
def two(func=None): return int(func(2)) if func else 2
def three(func=None): return int(func(3)) if func else 3
def four(func=None): return int(func(4)) if func else 4
def five(func=None): return int(func(5)) if func else 5
def six(func=None): return int(func(6)) if func else 6
def seven(func=None): return int(func(7)) if func else 7
def eight(func=None): return int(func(8)) if func else 8
def nine(func=None): return int(func(9)) if func else 9

def plus(func): return lambda x: x + func
def minus(func): return lambda x: x - func
def times(func): return lambda x: x * func
def divided_by(func): return lambda x: x // func


def main():
    assert seven(times(five())) == 35
    assert four(plus(nine())) == 13
    assert eight(minus(three())) == 5
    assert six(divided_by(two())) == 3


if __name__ == '__main__':
    main()
