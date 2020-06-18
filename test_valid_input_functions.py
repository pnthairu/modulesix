# Start Program
"""
Program: _testvalid_input_functions.py
Author: Paul Thairu
Last date modified: 06/017/2020

This unit test is for testing all senarios for user input that is
name of the score, score and message
"""


import unittest
from more_functions import valid_input_in_functions as test


class MyTestCase(unittest.TestCase):
    # testing only the test name
    def test_score_input_test_name(self):
        self.assertEqual(test.score_input('maths'), 'maths')

    # testing only the test name and score
    def test_score_input_test_name_and_score(self):
        self.assertEqual(test.score_input('maths', 10), 'maths', 10)

    # testing only the test name, score and  message
    def test_score_input_test_name_and_score_message(self):
        self.assertEqual(test.score_input('maths', 10, "invalid"), 'maths', 10, "invalid")

    # testing score which is less than zero (out of range)
    def test_score_input_test_name_and_score_message(self):
        self.assertEqual(test.score_input('maths', 0, "invalid"), 'maths', -10, "invalid")

    # testing score which is greater than 100 (out of range)
    def test_score_input_test_name_and_score_message(self):
        self.assertEqual(test.score_input('maths', 0, "invalid"), 'maths', 101, "invalid")


if __name__ == '__main__':
    unittest.main()
