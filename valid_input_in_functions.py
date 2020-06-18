# Start Program
"""
""
Program: valid_input_functions.py
Author: Paul Thairu
Last date modified: 06/017/2020

Write a function score_input() that takes (as parameter arguements) a test_name, test_score,
and invalid_message that validates the test_score, asking the user for a valid test score
until it is in the range, then prints valid input as 'Test name: ##'.
"""

"""
functions that takes one parameter that is name
"""
def score_input(test_name):
    return test_name

"""
    Function that takes two parameters that name ans score
"""
def score_input(test_name, test_score=0):
    return test_name, test_score

"""
Function that takes in three parameters that is name, score
and invalid message if the test score is not between 1 and 100
"""
def score_input(test_name, test_score=0, invalid_message=""):
    return test_name, test_score, invalid_message


if __name__ == '__main__':
# calling the first function
    """Prompts the user for test name """  # docstring
    test_name = input("Please test score name: ")  # user input string

    # Calling score_input function that has one parameter
    score_input(test_name)

    print(score_input(test_name))  # printing score_input(test_name) function

# calling the second function
    """Prompts the user for test name """  # docstring
    test_name = input("Please enter score name: ")  # user input string

    """Prompts the user for test score """  # docstring
    test_score = int(float(input("Please enter valid test score (1-100): ")))  # user input int, possible ValueError

    # Calling score_input function that has two parameter
    score_input(test_score, test_score)

    print(score_input(test_name, test_score))   # printing score_input(test_name_test_score) function

# Calling the third function score_input(test_name, test_score=0, invalid_message)
    """ Prompts the user for test name, test score and message"""  # docstring
    test_name = input("Please test score name: ")  # user input string

    """ Prompts the user for test score """  # docstring
    test_score = int(float(input("Please enter valid test score (1-100): ")))

    """ declaring the invalid message if the score is not in range """
    invalid_message = "Invalid test score, try again!!!!"""
    try:
        # checking in the score is in range
        if test_score < 0 or test_score > 100:
            print("Ops!! WRONG TEST SCORE")
            print(test_name, "", test_score, "", invalid_message)
    except ValueError:
        print(invalid_message)
    else:
        # calling score_input function that has three parameters that is
        # test_name, test_score, invalid_message
        score_input(test_name, test_score, invalid_message)

        # printing score_input(test_name, test_score, invalid_message) function
        print(score_input(test_name, test_score, invalid_message))

# End Program

