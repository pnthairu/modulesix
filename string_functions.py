# Start Program
"""
""
Program: valid_input_functions.py
Author: Paul Thairu
Last date modified: 06/017/2020

Write a function multiply_string() that takes a string message
and a number n and returns the string with message printed n times.
"""

# deckaring global varibales
lucky_number = range(1, 9)
name = "Paul Thairu"

# creating multiply_string function
def multiply_string(lucky_number):

    # Promt to enter lucky number
    lucky_number = int(input("What is your lucky number (1-9): "))

    # condition to check in lucky number is in range
    if lucky_number < 0 or lucky_number > 9:
        print("Opps lucky number not in range")
    else:
        for i in range(lucky_number):
            print(name)
        return lucky_number


if __name__ == '__main__':
    multiply_string(lucky_number) # function call

# End program
