import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):
    def setUp(result):
        result.calc = Calculator()
    def test_add(result):
        result.assertEqual(result.calc.add(5, 3), 8)
        result.assertEqual(result.calc.add(-2, 2), 0)
    def test_subtract(result):
        result.assertEqual(result.calc.subtract(5, 3), 2)
    def test_multiply(result):
        result.assertEqual(result.calc.multiply(4, 3), 12)
        result.assertEqual(result.calc.multiply(5, 0), 0)
if __name__ == "__main__":
    unittest.main()
