'''
The fraction 49/98 is a curious fraction, as an inexperienced mathematician in
attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is
correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less than
one in value, and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms,
find the value of the denominator.
'''
from itertools import permutations
from functools import reduce
from operator  import mul
from fractions import gcd

combs = list(permutations(range(1,10), r=2))
allstrs = list(map(lambda pair: str(pair[0]) + str(pair[1]), combs ))
combsagain = list(permutations(allstrs,r=2))

circapri = lambda pair: \
        int(pair[0][0]) / int(pair[1][1]) == int(pair[0]) / int(pair[1])
con = list(filter( circapri, combsagain ))
filterNum = lambda pair: pair[0][1] == pair[1][0]
commonNum = list(filter(filterNum,con))

Numerator = reduce(mul, list(map(lambda num: int(num[0][0]),commonNum)))
Denominator = reduce(mul, list(map(lambda num: int(num[1][1]),commonNum)))

def lcm(numbers):
    return reduce(lambda x,y: (x*y)/gcd(x,y), numbers, 1)

print(commonNum)
print(lcm( (Numerator, Denominator) ))
