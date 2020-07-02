import re
import unittest
from string_calculator.calc import Calculator

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()
    def tearDown(self):
        pass

    def test_EmptyString(self):
        self.assertEqual(self.calculator.add(''), 0)
    def test_SingleNumber(self):
        self.assertEqual(self.calculator.add('1'), 1)
    def test_TwoNumbers(self):
        self.assertEqual(self.calculator.add('1,3'), 4)
    def test_MultipleNumbers(self):
        self.assertEqual(self.calculator.add('1,2,3,4'), 10)
    def test_LineDelimeter(self):
        self.assertEqual(self.calculator.add('1,*S2\n*3'), 6)

if __name__ == '__main__':
    unittest.main()


