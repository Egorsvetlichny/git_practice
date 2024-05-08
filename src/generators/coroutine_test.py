def greeting():
    while True:
        name = yield
        print(f"Hello, {name}!")


def main():
    greet = greeting()
    next(greet)
    greet.send("Egor")
    greet.send("Alina")
    greet.send(123)
    greet.send(True)
    greet.send(324.423)
    greet.send(4 + 7j)
    greet.send([4, 2])
    greet.send((2, 3, 4))
    greet.send({1, 1, 3, 5, 1})
    greet.send({'few': 1, 'fe': 4})


if __name__ == '__main__':
    main()
