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

  primes = [2]
  for i in range(3,maxnum,2):
    if isPrime(i):
      primes.append(i)

  return sum(primes)

print(sumPrimes())
