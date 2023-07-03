# Programming-Challenge-

The ancient Egyptians could easily handle simple fractions, but with one remarkable peculiarity. The only fractions these ancients used were 2/3 and the reciprocals of the integers, the so-called unit fractions (1/n) with each numerator equal to 1. Curious though this treatment of fractions may seem to us, no doubt it was both natural and easy for the ancient Egyptians to use. Thus their answer to the problem, 'divide seven loaves among ten men' was not 7/10 of a loaf each, but the sum of two fractions 1/2 + 1/5.

Can all proper fractions be expressed as the sum of unit fractions, without repetition?

The answer is Yes, as the great Fibonacci showed in his Liber Abaci (circa 1202), where he described what is now called the greedy algorithm. For this example, the greedy algorithm is to repeatedly subtract the largest possible unit fraction, then do the same again, and so on until 0 is reached. Experimentally, we find that most fractions can be represented compactly in this manner of sums of unit fractions, and indeed there is a math proof (Sylvester, 1880) that applying a greedy algorithm to the fraction p/q, where p is less than q, always produces a sequence of terms with no more than p unit fractions.

For this homework you are to: Write a python program from scratch (with no starting code) which includes a function called "egypt", which has two integer arguments, say p and q, and uses the greedy approach outlined above to print out a listing representing a sum of unit fractions, with sum equal to p/q.

Here is a sample run:
>>> egypt(11,12)
1/2  + 1/3  + 1/12   = 11/12


You should use good style and documentation, including defining functions which use doctests. Below is an example of a set of appropriate doctests. Submit a single python file hw01.py on Canvas.


def egypt(n,d):
    """
    >>> egypt(3,4)
    '1/2 + 1/4 = 3/4'
    >>> egypt(11,12)
    '1/2 + 1/3 + 1/12 = 11/12 '
    """

## Partial credit will be given for code that passes the two given doctests. 
## For full credit on HW1 you should test your solutions to egypt(103,104) and  egypt(123,124)
## These are more difficult and may require you to develop faster, more efficient code.
## Hint: you may consider using code for gcd function for greatest common divisor:
## https://www.geeksforgeeks.org/gcd-in-python/

>>> egypt(123,124)
    '1/2 + 1/3 + 1/7 + 1/64 + 1/8333 + 1/347186112'
>>> egypt(103,104)
    '1/2 + 1/3 + 1/7 + 1/71 + 1/9122 + 1/141449381 + 1/100039636784966424'
