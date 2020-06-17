# Start Program
"""
""
Program: test_valid_input_functions.py
Author: Paul Thairu
Last date modified: 06/017/2020

Write a function multiply_string() that takes a string message
and a number n and returns the string with message printed n times.
"""

import unittest
from more_functions import string_functions as guess


class MyTestCase(unittest.TestCase):
    def test_something(self):
        # testing guess number is between 1 and 9
        self.assertEqual(guess.multiply_string("Paul Thairu"), 5)


if __name__ == '__main__':
    unittest.main()
