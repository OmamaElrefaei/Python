#This program was a MITx:  6.00.1x problem
"""
Created on Thursday, July 17, 01:10 PM 2019

@author: Omama Elrefaei for isWordGuessed, getGuessedWord, getAvailableLetters, hangman functions
"""


# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()


def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    
    comp = 0
    
    if len(lettersGuessed) == 0:
        return False
    
        
    else:
        for char in secretWord:
     
            if char in lettersGuessed:
                comp +=1
            else:
                comp -=1
        
        return comp == len(secretWord)
    
    



def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
 
    
    comp = ''
    
    if len(lettersGuessed) == 0:
        comp = '_ '
        return comp * len(secretWord)
    
        
    else:
        for char in secretWord:
     
            if char in lettersGuessed :
                comp += char
            else:
                comp +='_ '
        
        return comp
                
import string
def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    
    L =[]
    S = ''
    All_letter = string.ascii_lowercase
    
    if lettersGuessed == []:
        return All_letter
    
    else:
        for i in All_letter:
            L.append(i)
        
        for char in All_letter:
            if char in lettersGuessed:
                 L.remove(char)
    
        for j in L:
            S += j
             
        return S   
       

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''

    print("Welcome to the game, Hangman!" + "\n" + "I am thinking of a word that is " +str(len(secretWord))+' letters long.')
    print("-------------")
    
    lettersGuessed = ''
    repated = []
    mistakesMade = 0
    letters = ''
    guessesLeft = 8 - mistakesMade
    
    while mistakesMade < 8:
        
        print('You have ' + str(guessesLeft) +' guesses left.\nAvailable letters: ' + str(getAvailableLetters(lettersGuessed)))
        
        letters = input(str.lower('Please guess a letter: '))
        
        lettersGuessed += letters
        guessed = getGuessedWord(secretWord, lettersGuessed)
        
        if letters in repated:
            print("Oops! You've already guessed that letter: ", guessed)
            print("-------------")
        
        else:
            repated.append(letters)
       
        
        
            if isWordGuessed(letters, secretWord):

                print ('Good guess: ', guessed)
                print("-------------")
                
                if guessed == secretWord:
                    print('Congratulations, you won!')
                    break

            else:
    
                print ('Oops! That letter is not in my word: ' , guessed)
                print("-------------")
                mistakesMade += 1
                guessesLeft = 8 - mistakesMade
        
        
    if guessed != secretWord:
        print('Sorry, you ran out of guesses. The word was else.')


# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
