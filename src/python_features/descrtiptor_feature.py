# Атрибуты класса можно превратить в дескрипторы, изменив их стандартное поведение с помощью методов __get__, __set__
# или __delete__. Таким образом можно, например, запретить перезапись или удаление свойства.


import time


# First example
class MyDescriptor(object):
    def __init__(self, fget):
        self.fget = fget

    def __get__(self, obj, type):
        print("__get__({}, {})".format(obj, type))
        return self.fget(obj)


class MyClass(object):
    @MyDescriptor
    def foo(self):
        print("Foo!")


obj = MyClass()
obj.foo


# Second example
class ValidateAge:
    def __set_name__(self, owner, name):
        self.private_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.private_name, None)

    def __set__(self, instance, value):
        if not (0 <= value <= 100):
            raise ValueError("Возраст должен быть между 0 и 100 годами")
        setattr(instance, self.private_name, value)


class Person:
    age = ValidateAge()

    def __init__(self, name, age):
        self.name = name
        self.age = age


try:
    p = Person("Kolya", 30)  # валидный возраст
    print(p.age)
    p.age = -5  # невалидный возраст, будет вызвано исключение ValueError
except ValueError as e:
    print(e)


# Third example
class CachedAttribute:
    def __init__(self, method):
        self.method = method
        self.cache = {}

    def __get__(self, instance, owner):
        if instance not in self.cache:
            self.cache[instance] = self.method(instance)
        return self.cache[instance]


class HeavyComputation:
    @CachedAttribute
    def compute(self):
        # имитация длительного вычисления
        time.sleep(2)
        return "Результат вычисления"


hc = HeavyComputation()
start_time = time.time()
print(hc.compute)  # первый вызов занимает время
print(f"Выполнено за {time.time() - start_time} секунд")

start_time = time.time()
print(hc.compute)  # второй вызов мгновенный, использует кэшированный результат
print(f"Выполнено за {time.time() - start_time} секунд")


# Example №4
class LoggedAttribute:
    def __set_name__(self, owner, name):
        self.private_name = '__' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.private_name, None)

    def __set__(self, instance, value):
        print(f"Установка {self.private_name} в {value}")
        setattr(instance, self.private_name, value)


class User:
    name = LoggedAttribute()
    age = LoggedAttribute()

    def __init__(self, name, age):
        self.name = name
        self.age = age


u = User("Katya", 30)
u.name = "Katyuha"  # Логируется изменение
u.age = 31  # Логируется изменение

