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


# Example №5
class Singleton:
    def __init__(self, cls):
        self.cls = cls
        self.instance = None

    def __get__(self, instance, owner):
        if self.instance is None:
            self.instance = self.cls()
        return self.instance


class Database:
    def __init__(self):
        print("Создание базы данных")


# применение дескриптора Singleton
class AppConfig:
    db = Singleton(Database)


# тестирование паттерна Singleton
config1 = AppConfig()
config2 = AppConfig()
db1 = config1.db  # создание БД
db2 = config2.db  # не создает новый экземпляр, использует существующий

print(db1 is db2)  # выведет True, подтверждая, что db1 и db2 - один и тот же объект


# Example №6
class VehicleFactory:
    def __init__(self, cls):
        self.cls = cls

    def __get__(self, instance, owner):
        return self.cls()


class Car:
    @staticmethod
    def drive():
        print("Вождение автомобиля")


class Bike:
    @staticmethod
    def ride():
        print("Езда на велосипеде")


# фабрика, создающая автомобили
class AppConfigCar:
    vehicle = VehicleFactory(Car)


# фабрика, создающая велосипеды
class AppConfigBike:
    vehicle = VehicleFactory(Bike)


# создание и использование автомобиля
car_config = AppConfigCar()
car = car_config.vehicle  # создает объект Car
car.drive()

# создание и использование велосипеда
bike_config = AppConfigBike()
bike = bike_config.vehicle  # создает объект Bike
bike.ride()


# Example №7
# property - работает как дескриптор, используя методы __get__, __set__ и __delete__ для управления доступом к атрибуту
class Celsius:
    def __init__(self, temperature=0):
        self.__temperature = temperature

    @property
    def temperature(self):
        return self.__temperature

    def to_fahrenheit(self):
        return (self.__temperature * 1.8) + 32

    def get_temperature(self):
        print("Получение значения")
        return self.__temperature

    @temperature.setter
    def temperature(self, value):
        if value < -273.15:
            raise ValueError("Температура не может быть ниже -273.15 градусов Цельсия")
        print("Установка значения")
        self.__temperature = value


c = Celsius(37)
print(c.temperature)
c.temperature = -300  # вызовет исключение

# classmethod - реализован также как дескриптор. Когда метод декорирован как classmethod,
# его вызов приводит к вызову метода __get__ дескриптора, который возвращает привязанный метод - функцию,
# первым аргументом которой автоматически становится класс

# staticmethod - также реализован как дескриптор.
# При его использовании метод __get__ дескриптора просто возвращает функцию без привязки к экземпляру или классу
