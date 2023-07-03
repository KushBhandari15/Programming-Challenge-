# -*- coding: utf-8 -*-
"""
Created on Sun Sep 11 20:16:04 2022

@author: Kush Bhandari
"""

def egypt(n,d):
    """
    >>> egypt(3,4)
    1/2 + 1 / 4
    >>> egypt(11,12)
    1/2 + 1/3 + 1 / 12
    >>> egypt(123,124)
    1/2 + 1/3 + 1/7 + 1/64 + 1/8333 + 1 / 347186112
    >>> egypt(103,104)
    1/2 + 1/3 + 1/7 + 1/71 + 1/9122 + 1/141449381 + 1 / 100039636784966432
    """
    if (n%d==0):
        print( n/d)
    elif (d%n==0):
        print("1 /",int(d/n))
    
    elif (d>n):
        x=int(d/n) +1
        print("1/",end="")
        print(x,"+",end=" ")
        egypt((n*x)-d,d*x)

    elif(n>d):
        print(int(n/d),"+")
        egypt(n%d,d)

    else:
        print(0)
    
        
    
## Partial credit will be given for code that passes the two given doctests. 
## For full credit on HW1 you should test your solutions to egypt(103,104) and  egypt(123,124)
## These are more difficult and may require you to develop faster, more efficient code.
## Hint: you may consider using code for gcd function for greatest common divisor:
## https://www.geeksforgeeks.org/gcd-in-python/


import doctest
if __name__ == "__main__":
  doctest.testmod(verbose=True)

