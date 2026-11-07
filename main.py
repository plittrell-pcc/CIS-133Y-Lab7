# ***************************************************************************
#
# Author: Paul Littrell
# Lab:    CIS-133Y Lab 7
# Date:   November 6, 2026
# Desc:   Main driver program for the Census Name Viewer. Displays a menu,
#         validates user input, and uses N-tier architecture to fetch and
#         display Census Name objects from a live MSSQL database.
#
# Input:  Menu choices, year, and gender filters.
# Output: Formatted list of top 20 US Census Bureau name records.
# Source: Module 7 Lab 7
# GitHub: https://github.com/plittrell-pcc/CIS-133Y-Lab7
#
# ***************************************************************************

import Name as n
import valid as v


def print_welcome_message():
    print("===========================================================")
    print("                WELCOME TO CENSUS NAME VIEWER              ")
    print("===========================================================")
    print("This program fetches historical US Census Bureau name data ")
    print("from a live database using N-tier architecture.            ")
    print("                                                           ")
    print("Please follow the prompts below to filter the database!    \n")
    print("-----------------------------------------------------------\n")


def display_menu():
    print("--- MAIN MENU ---\n")
    print("1. Search Name Database")
    print("2. Quit Program")


def main():
    print_welcome_message()

    choice = 0
    while choice != 2:
        display_menu()

        # Re-using a basic input for the menu, or we could add get_menu_choice to valid.py
        try:
            choice = int(input("Enter your choice (1-2): "))
        except ValueError:
            print("Error: Please enter 1 or 2.")
            continue

        if choice == 1:
            print()
            # Fetch inputs using our updated valid.py constraints
            year = v.get_year()
            gender = v.get_gender()

            print(f"\n20 most popular names for {gender} babies in {year}:\n")

            # Print table headers with formatting
            print(f"  {'Year':<6} {'Name':<22} {'Gender':<8} {'Count':<7}")

            # Pass user inputs to the business layer
            names_list = n.Name.readNames(year, gender)

            if not names_list:
                print("  No records found for that combination.")
            else:
                for name_obj in names_list:
                    # Print formatted rows to match the header
                    print(f"  {name_obj.get_year():<6} "
                          f"{name_obj.get_name():<22} "
                          f"{name_obj.get_gender():<8} "
                          f"{name_obj.get_count():<7}")
            print("-" * 50 + "\n")

        elif choice == 2:
            print("\nThank you for using the Census Name Viewer. Goodbye!")
        else:
            print("Invalid choice, please enter 1 or 2.")


if __name__ == "__main__":
    main()