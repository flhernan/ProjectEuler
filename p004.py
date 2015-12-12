'''
A palindromic number reads the same both ways. The largest palindrome made
from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
'''

isPalindrome = lambda x: str(x) == str(x)[::-1]

print(max(filter(isPalindrome, [x*y for x in range(1,1000)
                                    for y in range(1,x+1)] )))
