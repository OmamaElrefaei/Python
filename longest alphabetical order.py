"""
Created on Tue Jul 9 11:56:40 2019

#@author: Omama Elrefaei
"""

def longest_alphabetical_order(s):
    
    """
    Returns: The longest substring of the string s in which the letters occur in alphabetical order
             rounded to 4 decimal places.
    s: a string of lower case characters.
    """

    longest = s[0]
    current = s[0]
 
    for i in range (len(s) - 1):

        if s[i+1] >= s[i]:
            current += s[i+1]
            if len(current) > len(longest):
                longest = current  
        else:
            current = s[i+1] 

    return str("Longest substring in alphabetical order is: " + str(longest))