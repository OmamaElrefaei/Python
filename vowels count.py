"""
Created on Tue Jul  9 11:56:40 2019

#@author: Omama Elrefaei
"""

def vowels_count(s):
    
    """
    Returns: The number of vowels contained in the string s. 
    s: a string of lower case characters.
    """
    
    count = 0
    for j in s:
        if j in ('a', 'e', 'i', 'o', 'u'):
            count += 1
    return str("Number of vowels: " + str(count))