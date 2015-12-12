from fractions import Fraction, gcd
from sys import setrecursionlimit

setrecursionlimit(10001)

def expansion(iterations):
    def expand(a, b, iterations):
        if iterations > 1:
            n, d = expand(a,b,iterations -1)
            a = 2*n + d
            b = n
            return (a,b)
        else:
            return ( 2, 1 )
    n, d = (0, 0)
    n, d = expand(n, d, iterations)

    return (n+d , n)


denominator = lambda n: Fraction(n).limit_denominator().denominator
numerator = lambda n: Fraction(n).limit_denominator().numerator

digitCount = lambda n: len(str(n))

biggerNumerator = lambda n: digitCount(n[0]) > digitCount(n[1])

result = list(filter(lambda num: biggerNumerator(expansion(num)), range(1, 1001)))
print(len(result))
