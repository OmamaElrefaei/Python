"""
Created on Fri Jul 12 03:17:38 2019

@author: Omama Elrefaei
"""

# Importing "math" for mathematical operations:
import math

#The function named polysum: 
def polysum(n, s):
    
    """
    Returns: the sum the area and square of the perimeter of the regular polygon
             rounded to 4 decimal places.
    n: the number of sides of the regular polygon.
    s: the  length of each side of the regular polygon.
    """
    
    #The area of a regular polygon is:
    area = (0.25*n*s**2)/(math.tan(math.pi/n))
    
    #The perimeter of a polygon is:
    perimeter = s*n
    
    #The square of the perimeter is:
    square = (perimeter)**2
    
    #The sum  of area and square of the perimeter of the regular polygon is:
    summation = area + square
    
    #Returning the summation the area and square of the perimeter of the regular polygon
    #rounded to 4 decimal places:
    return round(summation,4)