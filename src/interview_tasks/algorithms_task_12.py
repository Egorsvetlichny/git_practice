# Написать функцию, принимающую целое число секунд и возвращающую сколько это времени в формате HH:MM:SS,
# Если время превышает 99:59:59, верните false.

from typing import Union


# Например: Input(7275), Output(02:01:15)

# my solution
def parentheses_accuracy(number: int) -> Union[str, bool]:
    if number < 0 or number > 359999:
        return False

    hours = number // 3600
    minutes = (number - hours * 3600) // 60
    seconds = number - hours * 3600 - minutes * 60

    return f'{str(hours).zfill(2)}:{str(minutes).zfill(2)}:{str(seconds).zfill(2)}'


# optimal solution
def optimal_parentheses_accuracy(number: int) -> Union[str, bool]:
    return f'{(number // 3600):02d}:{(number % 3600 // 60):02d}:{(number % 60):02d}' if 0 <= number <= 359999 else False


def main():
    assert optimal_parentheses_accuracy(7275) == '02:01:15'
    assert optimal_parentheses_accuracy(66666) == '18:31:06'
    assert optimal_parentheses_accuracy(359999) == '99:59:59'
    assert optimal_parentheses_accuracy(0) == '00:00:00'
    assert optimal_parentheses_accuracy(360000) is False
    assert optimal_parentheses_accuracy(-3213) is False


if __name__ == '__main__':
    main()
