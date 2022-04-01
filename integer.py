#!/usr/bin/env python3

# Created by: Nicolas Riscalas
# Created on: March 29 2022
# Game for random number


import sys


def main():
    # this function checks if there is over 30 students

    # input
    users_num = int(input("What number would you like to test "))
    if users_num > 0:
        print("Your number is positive")
    elif users_num < 0:
        print("Your number is negative")
    else:
        print("Your number is equal to 0")

    try_again = str(input("Would you like to try again? \n"))
    if try_again == "Y" or try_again == "y" or try_again == "yes" or try_again == "YES":
        main()
    elif try_again == "N" or try_again == "n" or try_again == "no" or try_again == "NO":
        sys.exit()


if __name__ == "__main__":
    main()
