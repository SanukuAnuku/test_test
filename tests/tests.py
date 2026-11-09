from unittest import TestCase
from app import calc

class TestCalcMethods(TestCase):
    def test_calc(self):
        self.assertEqual(calc(1, 2), 3)

    def test_sub(self):
        a = self.assertEqual(calc(1, 0), 1)
        with self.assertRaises(TypeError):
            a = divide(1, 0)
            print(a)

if __name__ == '__main__':
    tests = TestCalcMethods()
    tests.test_calc()
    tests.test.divide