from itertools      import takewhile, product
from sys            import maxsize
from math import sqrt

def isPrime(num):
    if num == 2:
        return True

    if num % 2 == 0 or num < 2:
        return False

    i = 3
    sqrtOfNum = sqrt(num)

    while i <= sqrtOfNum:
        if num % i == 0:
            return False
        i = i+2

    return True

a_numbers = list(range(-999, 1000))
b_numbers = list(filter( isPrime, range(1000) ))
ab_pairs = list(product( a_numbers, b_numbers ))

def quad_returns_primes(ab_pair):
    a, b = ab_pair
    return lambda n: isPrime(n**2 + a*n + b)

number_of_consecutive_primes=\
    lambda ab_pair:\
        len(list(takewhile( quad_returns_primes(ab_pair), range(maxsize) )))

result = list(map( number_of_consecutive_primes, ab_pairs ))
best_pair = result.index( max(result) )
a,b = ab_pairs[best_pair]
print("Best pair: (%d,%d)\nTheir product is: %d" % (a, b, a * b))
