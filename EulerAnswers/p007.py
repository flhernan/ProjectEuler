"""
Problem 7
---------
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that:
the 6th prime is 13.

What is the 10 001st prime number?
"""
from eulerFunctions import isPrime

def getPrimeAtIndex(index):

  primes = [2]
  x = 3

  while len(primes) < index:
    if isPrime(x):
      primes.append(x)
    x += 2

  return primes[-1]

print(getPrimeAtIndex(10001))
