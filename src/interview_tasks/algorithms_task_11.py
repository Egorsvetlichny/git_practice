# Написать функцию, принимающую строку и подсчитывающую корректность круглых скобок в ней.

# Например: Input('hey) i a, (fwe(())fw(r)'), Output(false)


def parentheses_accuracy(string: str) -> bool:
    counter = 0
    for char in string:
        if char == '(':
            counter += 1
        elif char == ')':
            counter -= 1

        if counter < 0:
            return False

    return counter == 0


def main():
    assert parentheses_accuracy('()') is True
    assert parentheses_accuracy('(') is False
    assert parentheses_accuracy(')') is False
    assert parentheses_accuracy('((()()())())()()') is True
    assert parentheses_accuracy('') is True
    assert parentheses_accuracy('hey) i a, (fwe(())fw(r)') is False
    assert parentheses_accuracy('(hey) i a, (fwe(r(g r e) e)f w(r )rw ) rwe') is True
    assert parentheses_accuracy('(()') is False
    assert parentheses_accuracy(') (') is False


if __name__ == '__main__':
    main()
