"""
Problem 5
---------
2520 is the smallest number that can be divided by each of the numbers from 1
to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the
numbers from 1 to 20?
"""
from eulerFunctions import isPrime
from functools import reduce
from operator import mul

def primeFactors(n):
    if n == 1:
        return [(1,1)]

    if isPrime(n):
        return [(n,1)]

    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)

    factorPairs = []
    for i in set(factors):
        factorPairs.append( (i, factors.count(i)) )

    return factorPairs

def smallestDivNum(n):
    if n == 1:
        return 1

    divPairs = []
    for i in range(1, n + 1):
        divPairs += primeFactors(i)

    divPairs = sorted(list(set(divPairs)))
    primes = list(filter(isPrime, range(n + 1)))
    result = []

    for i in primes:
        counts = list(filter(lambda pair: pair[0] == i, divPairs))
        maxPair = max(counts)
        result += [maxPair[0]] * maxPair[1]

    product = reduce(mul, result)
    return product

print(smallestDivNum(20))
