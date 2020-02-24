# Is in bisection search.

"""
Created on Sat Oct  5 12:11:16 2019

@author: Omama Elrefaei
"""

def isIn(char, aStr):
    
    """
    Returns: True if char is in aStr; False otherwise.
    char: a single character
    aStr: an alphabetized string
    
    """
    
    l = int(len(aStr)/2)
    lower = aStr[0: l-1]
    higher = aStr[l+1: len(aStr)]


    if len(aStr) == 0:
        return False
    elif len(aStr) == 1:
        return char == aStr[0]

    elif char > aStr[l]:
       aStr = higher
       
    elif char < aStr[l]:
       aStr = lower
    
    else:
        return char == aStr[l]
        
    return isIn(char, aStr)
       