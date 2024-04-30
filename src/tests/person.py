import time


class Person:
    normal_sleep_time = 8 * 60 * 60

    def __init__(self, name):
        self.name = name

    @staticmethod
    def eat():
        time.sleep(20 * 60 * 60)
        print('person has eaten!')
        return True

    @staticmethod
    def get_game(value):
        if value == 1:
            return 'Football'
        elif value == 2:
            return 'Hide and seek'
        elif value == 3:
            return 'Volleyball'
        else:
            return 'Computer games'

    def play(self):
        print(f'Person started playing!')
        res1 = self.get_game(1)
        res2 = self.get_game(2)
        res3 = self.get_game(576)
        time.sleep(120 * 60 * 60)
        print(f'Person has played {res1}, {res2} and {res3}!')
        return (res1 + res2 + res3).replace(' ', '')

    @staticmethod
    def work(sleep_time=normal_sleep_time, got_eat=True):
        if type(sleep_time) not in (int, float) or type(got_eat) != bool:
            raise TypeError("Неверный тип данных одного из аргументов!")
        if sleep_time <= 0 or sleep_time > 11 * 60 * 60:
            raise ValueError("Время сна должно быть положительным числом меньше 11!")
        if not got_eat or sleep_time < Person.normal_sleep_time:
            return False
        return True

    def do_some_things(self):
        print('Person started doing some things')

        # Долгая функция
        self.eat()
        self.play()

        print('Person has done some things!')
        return True
