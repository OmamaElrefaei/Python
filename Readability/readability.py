# A program that computes the approximate grade level needed to comprehend some text.

"""
Created on Monday, January 13, 2:26 PM 2020

#@author: Omama Elrefaei
"""

#cs50 is a library for Python
from cs50 import get_string
import string

# Asks the user to type in some text:
Text = get_string("Text: ")

letters = 0
words = 1
sentences = 0

for char in Text:
    # Count the number of letters:
    if char.isalpha() == True:
        letters += 1
    # Count the number of words:
    if char in string.whitespace:
        words += 1
    # Count the number of sentences:
    if char == "." or char == "?":
        sentences += 1

# The Coleman-Liau index:
index = (0.0588 * (letters / words) * 100) - (0.296 * (sentences / words) * 100) - 15.8

if index >= 16:
    print("Grade 16+")
elif index < 1:
    print("Before Grade 1")
else:
    print("Grade ", round(index))