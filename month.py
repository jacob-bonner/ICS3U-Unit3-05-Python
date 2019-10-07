#!/usr/bin/env python3

# Created by: Jacob Bonner
# Created on: October 2019
# This program outputs a month in accordance with a number the user enters


def main():
    # This function outputs a month in accordance with a number the user enters

    # Input
    month_number = \
        int(input("Enter your month number between 1-12 (integer): "))
    print("")

    # process
    if month_number == 1:
        # Output 1
        print("Your month is January")
    elif month_number == 2:
        # Output 2
        print("Your month is February")
    elif month_number == 3:
        # Output 3
        print("Your month is March")
    elif month_number == 4:
        # Output 4
        print("Your month is April")
    elif month_number == 5:
        # Output 5
        print("Your month is May")
    elif month_number == 6:
        # Output 6
        print("Your month is June")
    elif month_number == 7:
        # Output 7
        print("Your month is July")
    elif month_number == 8:
        # Output 8
        print("Your month is August")
    elif month_number == 9:
        # Output 9
        print("Your month is September")
    elif month_number == 10:
        # Output 10
        print("Your month is October")
    elif month_number == 11:
        # Output 11
        print("Your month is November")
    elif month_number == 12:
        # Output 12
        print("Your month is December")
    else:
        # Output 13
        print("Error, unable to identify integer")


if __name__ == "__main__":
    main()
