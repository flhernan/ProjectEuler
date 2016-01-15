"""
Problem 10
----------
The sum of the primes below 10 is
2 + 3 + 5 + 7 = 17.

Find the sum of all the primes
below two million.
"""
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

def sumPrimes(maxnum = 2000000):

  primes = [2] + list(filter(isPrime, range(3,maxnum,2)))
  return sum(primes)

print(sumPrimes())
