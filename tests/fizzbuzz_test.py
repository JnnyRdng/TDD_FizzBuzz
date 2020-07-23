import unittest
from modules.fizzbuzz import fizzbuzz

class TestFizzbuzz(unittest.TestCase):

    def test_fizz(self):
        result = fizzbuzz(3)
        self.assertEqual("Fizz", result)
        
    def test_buzz(self):
        result = fizzbuzz(5)
        self.assertEqual("Buzz", result)

    def test_fizzbuzz(self):
        result = fizzbuzz(15)
        self.assertEqual("FizzBuzz", result)

    def test_not_fizzbuzz(self):
        result = fizzbuzz(8)
        self.assertEqual("8", result)

    def test_mult_of_3(self):
        result = fizzbuzz(9)
        self.assertEqual("Fizz", result)

    def test_mult_of_5(self):
        result = fizzbuzz(25)
        self.assertEqual("Buzz", result)

    def test_with_strings(self):
        result = fizzbuzz("3")
        self.assertEqual("Fizz", result)