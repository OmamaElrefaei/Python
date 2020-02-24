#Luhn’s Algorithm.
#A program that prompts the user for a credit card number and then reports (via printf) whether it is a valid American Express, MasterCard, or Visa card number, per the definitions of each’s format herein

"""
Created on Friday, January 10, 8:41 PM 2020

#@author: Omama Elrefaei
"""

#cs50 is a library for Python.
from cs50 import get_int


def main():

    # Ask the user for the credit card number:
    Number = get_int("Please enter your credit card number: \n")

    # Print out the number:
    print(f"Number: {Number}\n")

    # Count the digits of the input numbers:
    num = [int(x) for x in str(Number)]
    Count = len(num)

    # Determine the first start number:
    FristOneDigit = num[0]
    # Determine the first two start numbers:
    FristTwoDigits = int("".join(map(str, num[0:2])))

    # Check if inputs are credit card numbers:
    if Count >= 13:
        if CheckLuhnAlg(num, Count):
            print(defcard(Count, FristOneDigit, FristTwoDigits))
    else:
        print("INVALID")

# Implement Luhn’s Algorithm:


def CheckLuhnAlg(num, Count):

    NonMultiDigit = []
    MultiDigit = []

    for Digits in num[Count-2:: -2]:
        MultiDigit.append(int(Digits*2 / 10) + Digits*2 % 10)
    for Digits in num[Count:: -2]:
        NonMultiDigit.append(Digits)

    SumMultiDigit = sum(MultiDigit)
    SumNonMultiDigit = sum(NonMultiDigit)
    CheckLuhn = SumMultiDigit + SumNonMultiDigit

    if CheckLuhn % 10 == 0:
        return True

    return False


def defcard(Count, FristOneDigit, FristTwoDigits):
    # American Express uses 15-digit numbers and start with 34, 37:
    if Count == 15 and FristTwoDigits in [34, 37]:
        return "AMEX"

    # MasterCard uses 16-digit numbers and start with 51, 52, 53, 54, or 55:
    # VISA uses 16-digit numbers and start with 4:
    elif Count == 16:
        if FristTwoDigits in [51, 52, 53, 54, 55]:
            return "MASTERCARD"
        elif FristOneDigit == 4:
            return "VISA"

    # Visa uses 13- and 16-digit numbers and start with 4:
    elif Count in [13, 16] and FristOneDigit == 4:
        return "VISA"

    return "INVALID"


main()
