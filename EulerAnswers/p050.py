from eulerFunctions import isPrime
from itertools import takewhile, dropwhile

primes = list(filter(isPrime, range(1, 500000, 2) ))[:1000]

limit = 1000000
sumprimes = []
lowBounds = range(0, len(primes))
for lowBound in lowBounds:
    summing = lambda n: sum(primes[lowBound:n])
    highBounds = range(lowBound + 1, len(primes))
    sumprime = list(map(summing, highBounds))
    sumprime = list(takewhile( lambda n: n < limit, sumprime ))
    sumprime = list(map(lambda num: (sumprime.index(num), num), sumprime ))
    maxsumprime = max(filter(lambda pair: isPrime(pair[1]), sumprime))
    if maxsumprime[0] < 400:
        break
    sumprimes.append( maxsumprime )

print(max(sumprimes))
