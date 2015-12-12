'''
Problem 10
----------
The sum of the primes below 10 is
2 + 3 + 5 + 7 = 17.

Find the sum of all the primes
below two million.
'''
from eulerFunctions import isPrime

def sumPrimes(maxnum = 2000000):

  primes = [2] + list(filter(isPrime, range(3,maxnum,2)))
  return sum(primes)

print(sumPrimes())
