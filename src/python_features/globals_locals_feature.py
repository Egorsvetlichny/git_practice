killer = 'Ivan Ivanov'


def func(atr_age):
    first_name = 'Jogn'
    last_name = 'Wick'
    age = atr_age
    price_for_head = 10_000.99

    def kill_john(weapon='gun'):
        killer_name = killer
        print(f'locals and globals of "{kill_john.__name__}" function:')
        print(locals())
        print(globals())

    print(f'locals and globals of "{func.__name__}" function:')
    print(locals())
    print(globals())
    print()

    kill_john()


if __name__ == '__main__':
    func(41)
