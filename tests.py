from main import Calculator
import unittest


class TestCalculator(unittest.TestCase):

    def test_circle_area(self):
        self.assertAlmostEqual(Calculator.circle_area(5), 78.53981633974483)

        with self.assertRaises(ValueError):
            Calculator.circle_area(-1)

    def test_triangle_area(self):
        self.assertAlmostEqual(Calculator.triangle_area(3, 4, 5), 6)

        with self.assertRaises(ValueError):
            Calculator.triangle_area(3, -4, 5)

        with self.assertRaises(ValueError):
            Calculator.triangle_area(1, 1, 10)

    def test_custom_area(self):
        self.assertAlmostEqual(Calculator.custom_area(5), 78.53981633974483)

        self.assertAlmostEqual(Calculator.custom_area(3, 4, 5), 6)

        with self.assertRaises(ValueError):
            Calculator.custom_area(1, 2)

    def test_is_rat(self):
        self.assertTrue(Calculator.is_rat(3, 4, 5))

        self.assertFalse(Calculator.is_rat(1, 1, 1))

        with self.assertRaises(ValueError):
            Calculator.is_rat(3, 4, -5)


if __name__ == '__main__':
    unittest.main()
