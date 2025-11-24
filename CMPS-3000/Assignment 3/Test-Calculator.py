import unittest
from Calculator import add, subtract, multiply, divide

class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2,3),5)
        self.assertEqual(add(-1,1),0)

    def test_subtract(self):
        self.assertEqual(subtract(5,3),2)

    def test_multiply(self):
        self.assertEqual(multiply(4,2),8)

    def test_divide(self):
        self.assertEqual(divide(10,2),5)

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            divide(5,0)

if __name__ == "__main__":
    unittest.main()