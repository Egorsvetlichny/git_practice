class Person:
    normal_sleep_time = 8 * 60 * 60

    def __init__(self, name):
        self.name = name

    def eat(self):
        pass

    @staticmethod
    def work(sleep_time=normal_sleep_time, got_eat=True):
        if not got_eat or sleep_time < Person.normal_sleep_time:
            return False
        return True
