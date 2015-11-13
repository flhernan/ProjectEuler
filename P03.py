'''
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
'''
from math import sqrt

N = 600851475143
rootN = (int)(sqrt(N))
isFactor = lambda x: N % x==0
factors = list(filter( isFactor, [x for x in range(2,rootN)]))
primes = factors.copy()
for i in factors:
  for j in range(2,i):
    if(i%j == 0):
      if(i in primes):
        primes.remove(i)
print(primes)
