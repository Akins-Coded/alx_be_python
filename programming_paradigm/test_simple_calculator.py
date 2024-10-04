import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the addition method."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(-7, 1), -6)
        self.assertEqual(self.calc.add(9, -3), 6)
       

# subtract
    def test_subtraction(self):
            """Test the Subtraction method."""
            self.assertEqual(self.calc.subtract(2, 3), -1)
            self.assertEqual(self.calc.subtract(3, 2), 1)
            self.assertEqual(self.calc.subtract(-3, -2), -1)
            self.assertEqual(self.calc.subtract(7, -2), 9)
# multiply
    def test_multiply(self):
         self.assertEqual(self.calc.multiply(-1, 1), -1)
         self.assertEqual(self.calc.multiply(-1, -1), 1)
         self.assertEqual(self.calc.multiply(-1, 0), 0)
         self.assertEqual(self.calc.multiply(3, 2), 6)

#divide.
    def test_dividion(self):
         self.assertEqual(self.calc.divide(-10,10), -1)
         self.assertEqual(self.calc.divide(-5, -5), 1)
         self.assertEqual(self.calc.divide(12, 4), 3)
         self.assertEqual(self.calc.divide(1, -1), -1)

         with self.assertRaises(ValueError):
              self.calc.divide(5,0)
if __name__ == "__main__":
     unittest.main()