import math


class Calculator:

    @staticmethod
    def circle_area(radius):

        if radius <= 0:
            raise ValueError("A non-positive radius has been detected!")

        return math.pi * radius ** 2

    @staticmethod
    def triangle_area(a, b, c):

        if any(side <= 0 for side in (a, b, c)):
            raise ValueError("A non-positive side has been detected!")

        half_p = (a + b + c) / 2
        arr = [half_p - a, half_p - b, half_p - c]
        if any(temp <= 0 for temp in arr):
            raise ValueError("The triangle does not exist (the sum of the two sides is less than the third).")
        return math.sqrt(half_p * arr[0] * arr[1] * arr[2])

    @classmethod
    def custom_area(cls, *args):

        dims = len(args)

        match dims:
            case 1:
                return cls.circle_area(args[0])
            case 3:
                return cls.triangle_area(args[0], args[1], args[2])
            case default:
                raise ValueError("Unsupported number of arguments. Only 1 or 3 arguments are supported.")

    @staticmethod
    def is_rat(a, b, c):
        sorted_sides = sorted([a, b, c])
        if any(side <= 0 for side in sorted_sides):
            raise ValueError("A non-positive side has been detected!")
        return sorted_sides[0] ** 2 + sorted_sides[1] ** 2 == sorted_sides[2] ** 2
