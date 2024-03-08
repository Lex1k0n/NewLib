from math import sqrt


class Square:

    @classmethod
    def triangle(cls, a: float, b: float, c: float) -> float:
        p = a + b + c
        return sqrt(p * (p - a) * (p - b) * (p - c))

    @classmethod
    def is_rect(cls, a: float, b: float, c: float) -> bool:
        return a ** 2 + b ** 2 == c ** 2 or c ** 2 + b ** 2 == a ** 2 or a ** 2 + c ** 2 == b ** 2
