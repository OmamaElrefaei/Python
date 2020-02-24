#Greedy Algorithm.
#A program that first asks the user how much change is owed and then prints the minimum number of coins with which that change can be made.

"""
Created on Friday, January 10, 9:28 PM 2020

#@author: Omama Elrefaei
"""

#cs50 is a library for Python.
from cs50 import get_float

# Ask the user how much change is owed:
Change = get_float("How much change is owed?")
print(f"Change owed: {round(Change,2)}")

# Check If the user fails to provide a non-negative value:
while Change < 0:
    Change = get_float("how much change is owed?")
    print(f"Change owed: {round(Change,2)}")

# Count the minimum number of coins possible:
Cents = round(Change * 100)
MinNumOfCoins = 0

if (Cents >= 25):

    MinNumOfCoins += (int)(Cents / 25)
    Cents %= 25

# Numbers of Dimes:
if Cents < 25 and Cents >= 10:

    MinNumOfCoins += (int)(Cents / 10)
    Cents %= 10

# Numbers of Nickels:
if Cents < 10 and Cents >= 5:

    MinNumOfCoins += (int)(Cents / 5)
    Cents %= 5

# Numbers of Pennies:
if Cents < 5:

    MinNumOfCoins += Cents


print(MinNumOfCoins)
