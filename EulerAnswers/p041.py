from itertools import permutations
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

pans = list(permutations('1234567', r=7))
print(len(pans))
joinNint = lambda tup : int(''.join(tup))
pans = list(map(joinNint, pans))
primepans = list(filter(isPrime,pans))
print(max(primepans))
