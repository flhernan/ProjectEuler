from eulerFunctions import isPrime
from itertools import dropwhile
from math import sqrt
isOdd = lambda num: num % 2 == 1
isComposite = lambda num: not isPrime(num)
oddComposites = list(filter(lambda num: isOdd(num) and isComposite(num), range(9,10000)))

def isConjecture(num):
    primes = list(filter( isPrime, range(num) ))
    conjecture = lambda prime: sqrt((num - prime) / 2)== int(sqrt((num-prime) /2))
    return any(map(conjecture, primes))
result = list(dropwhile(lambda num: isConjecture(num), oddComposites))
print(result[0])
