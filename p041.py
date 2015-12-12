from eulerFunctions import isPrime
from itertools import permutations

pans = list(permutations('1234567', r=7))
print(len(pans))
joinNint = lambda tup : int(''.join(tup))
pans = list(map(joinNint, pans))
primepans = list(filter(isPrime,pans))
print(max(primepans))
