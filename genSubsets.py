"""
Created on Wed Oct 23 03:58:29 2019

@author: Omama Elrefaei
"""

def genSubsets(L):
    
    """
    Returns: all of the subsets of a list.
    L: a list.
    """
    
    if len(L) == 0:
        #list of empty list
        return [[]] 
    
    # all subsets without last element 
    smaller = genSubsets(L[:-1]) 
    # create a list of just last element
    extra = L[-1:]  
    new = [] 
    
    # for all smaller solutions, add one with last element 
    for small in smaller: 
        
        new.append(small+extra)  
    
    # combine those with last element and those without
    return smaller+new 
