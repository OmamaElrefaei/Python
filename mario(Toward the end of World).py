#Toward the end of World 1-1 in Nintendo’s Super Mario Brothers, Mario must ascend right-aligned pyramid of blocks, a la the below.
#In this program I allow the user to decide just how tall the pyramid should be by first prompting them for a positive integer between, say, 1 and 8, inclusive.

"""
Created on Friday, January 10,10:50 PM 2020

@author: Omama Elrefaei
"""

#cs50 is a library for Python.
from cs50 import get_int

# Asked the user How tall the pyramids should be?:
Height = get_int("How tall the pyramids should be?\n")

# To check if the input out of the range:
while (Height <= 0 or Height > 8):
    Height = get_int("please choose an integer number between 1 and 8\n")

# Building the pyramids:
for i in range(0, Height):

    for j in range(Height, i+1, -1):
        print(end=" ")

    for j in range(0, i+1):
        print("#", end="")

    # ending line after each row
    print("")