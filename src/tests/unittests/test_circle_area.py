import unittest

from tests.circle_area import get_circle_area
import math


class TestGetCircleArea(unittest.TestCase):
    def test_get_area(self):
        self.assertEqual(get_circle_area(5), math.pi * 25)
        self.assertEqual(get_circle_area(5.67), math.pi * 5.67 ** 2)
        self.assertEqual(get_circle_area(0.000000001), math.pi * 0.000000001 ** 2)
        self.assertEqual(get_circle_area(1), math.pi)

    def test_negative(self):
        self.assertRaises(ValueError, get_circle_area, -2424)
        self.assertRaises(ValueError, get_circle_area, -0.00000001)

    def test_zero(self):
        self.assertRaises(ValueError, get_circle_area, 0)

    def test_types(self):
        self.assertRaises(TypeError, get_circle_area, '5')
        self.assertRaises(TypeError, get_circle_area, True)
        self.assertRaises(TypeError, get_circle_area, [5])
        self.assertRaises(TypeError, get_circle_area, (0,))
        self.assertRaises(TypeError, get_circle_area, {0})
        self.assertRaises(TypeError, get_circle_area, None)
        self.assertRaises(TypeError, get_circle_area, 5 + 5j)
        self.assertRaises(TypeError, get_circle_area, 'five')
