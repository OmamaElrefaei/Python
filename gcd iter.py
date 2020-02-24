#The greatest common divisor of two positive integers.

"""
Created on Sat Oct  5 04:29:59 2019

@author: Omama Elrefaei
"""

from fractions import Fraction 
def gcdIter(a, b):
    
    """ 
    Rreturns: a positive integer, the greatest common divisor of a & b.
    a, b: positive integers
    """
    
    if a == 0 or a % b == 0:
        return b
    elif b == 0 or b % a == 0:
        return a
    else:
        return int(a/(Fraction(a, b).numerator))
    
    
# or
        
"""
def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    testValue = min(a, b)

    # Keep looping until testValue divides both a & b evenly
    while a % testValue != 0 or b % testValue != 0:
        testValue -= 1

    return testValue
"""