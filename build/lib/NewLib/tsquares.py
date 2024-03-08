from math import sqrt


class Square():

    @classmethod
    def triangle(cls, a: float, b: float, c: float):
        p = a + b + c
        return sqrt(p * (p - a) * (p - b) * (p - c))
