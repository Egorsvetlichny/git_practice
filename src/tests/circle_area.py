# Написать функцию, высчитывающую площадь окружности с заданным радиусом.
import math
from typing import Union


def get_circle_area(radius: Union[int, float]) -> Union[int, float]:
    if type(radius) not in (int, float):
        raise TypeError(f"Радиус окружности не может быть типа {type(radius)}")
    if radius < 0:
        raise ValueError("Радиус окружности не может быть отрицательным числом")
    if radius == 0:
        raise ValueError("Радиус окружности не может ровняться 0")
    return math.pi * radius ** 2


if __name__ == '__main__':
    pass
