import unittest
from my_package import calc

class TestCulculate(unittest.TestCase):
    def test_calc(self):
        self.assertEqual(calc(5, 6, '+'), 11)
        self.assertEqual(calc(5, -6, '*'), -30)
        self.assertEqual(calc(-5, -6, '*'), 30)
        self.assertEqual(calc(30, 6, '/'), 5)
        self.assertEqual(calc(5, -6, '-'), 11)

    def test_values(self):
        self.assertRaises(TypeError,calc,'5', True, 4 )


