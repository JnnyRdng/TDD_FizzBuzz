import unittest
from modules.fizzbuzz import fizzbuzz

class TestFizzbuzz(unittest.TestCase):

    def test_fizz(self):
        result = fizzbuzz(3)
        self.assertEqual("Fizz", result)
        
    def test_buzz(self):
        result = fizzbuzz(5)
        self.assertEqual("Buzz", result)