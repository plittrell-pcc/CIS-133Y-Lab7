# ***************************************************************************
#
# Author: Paul Littrell
# Lab:    CIS-133Y Lab 7
# Desc:   Utility module for validating user input. Contains functions to
#         safely get formatted integers (Year) and characters (Gender)
#         without crashing the program.
#
# ***************************************************************************

def get_year(prompt="Select a year between 1915 and 2014: "):
    """
    Prompts the user for a whole number between 1915 and 2014.
    """
    is_valid = False
    while not is_valid:
        try:
            num = int(input(prompt))
            if 1915 <= num <= 2014:
                return num
            else:
                print("The year must be between 1915 and 2014!")
        except ValueError:
            print("Please enter a whole number!")

def get_gender(prompt="Please enter a gender (M/F): "):
    """
    Prompts the user for a valid gender (M or F).
    """
    is_valid = False
    while not is_valid:
        val = input(prompt).strip().upper()
        if val in ('M', 'F'):
            return val
        else:
            print("Please type M or F!")