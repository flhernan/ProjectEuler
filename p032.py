"""
We shall say that an n-digit number is pandigital if it makes use of all the
digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1
through 5 pandigital.

The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing
multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can
be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to only
include it once in your sum.
"""
from itertools import combinations

def pandigitalProduct(ab):
    a,b = ab
    if len(str(a)) > 2 or len(str(b)) < 3 or len(str(a*b)) < 4: return 0
    identity = ''.join(sorted(str(a) + str(b) + str(a*b)))
    if len(identity) != 9:          return 0
    if identity == "123456789":     return a * b
    else:                           return 0
print(sum(set(map( pandigitalProduct, combinations(range(1,5000), 2) ))))
