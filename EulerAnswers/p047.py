from math import sqrt
from itertools import dropwhile

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

def distinctPrimeFactors(num):
    isFactor = lambda n: num % n == 0
    factorsSmall = list(filter(isFactor, range(1,(int)(sqrt(num)) +1 )))
    factorsLarge = list(map(lambda n: int(num/n) , factorsSmall))
    factors = factorsSmall + factorsLarge

    factors = list(filter(isPrime, factors))
    return factors

composites = list(filter(lambda n: not isPrime(n), range(2,200000)))
consec = lambda num: all(map(lambda n: len(distinctPrimeFactors(n)) == 4, list(range(num, num+4)) ))
result = list(dropwhile(lambda n: not consec(n), composites ))
print(result[0])
