class Person:
    normal_sleep_time = 8 * 60 * 60

    def __init__(self, name):
        self.name = name

    def eat(self):
        pass

    @staticmethod
    def work(sleep_time=normal_sleep_time, got_eat=True):
        if type(sleep_time) not in (int, float) or type(got_eat) != bool:
            raise TypeError("Неверный тип данных одного из аргументов!")
        if sleep_time <= 0 or sleep_time > 11 * 60 * 60:
            raise ValueError("Время сна должно быть положительным числом меньше 11!")
        if not got_eat or sleep_time < Person.normal_sleep_time:
            return False
        return True
