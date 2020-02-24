# Guess my number.

"""
Created on Wed Oct  2 02:43:33 2019

@author: Omama Elrefaei
"""

print("Please think of a number between 0 and 100!")

high = 100
low = 0
guessed = False

while not guessed:
    avrg = int((low + high) / 2)
    print("Is your secret number", avrg, "?")
    limit = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. c")
    
    if limit == "h":
        high = avrg
        
    elif limit == "l":
        low = avrg
    
    elif limit == "c":
        guessed = True
        
    else:
        print("Sorry, I did not understand your input.")
    
print("Game over. Your secret number was: ", avrg)

