"""
Created on Tue Jul  9 11:56:40 2019

#@author: Omama Elrefaei
"""

def bob_length(s):

    """
    Returns: the number of times the string 'bob' occurs in the string s.
    s: a string of lower case characters
    """
    
    bob =0

    for b in range(len(s)- 2):
        if s[b] == 'b' and s[b+1] =='o' and s[b+2] =='b':
                bob += 1
    return str('Number of times bob occurs is: ' + str(bob))