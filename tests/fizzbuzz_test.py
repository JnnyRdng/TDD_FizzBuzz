import unittest
from modules.fizzbuzz import fizzbuzz

class TestFizzbuzz(unittest.TestCase):

    def test_fizzbuzz(self):
        result = fizzbuzz(3)
        self.assertEqual("Fizz", result)
        