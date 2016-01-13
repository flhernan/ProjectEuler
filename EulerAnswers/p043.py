from itertools import permutations
from eulerFunctions import isPrime

pandigitals = list(map( lambda string: ''.join(string),\
        list(permutations('0123456789', r=10))))

def subStringDivisible(string):
    primes = list(filter( isPrime, range(2,18) ))
    return all(list(map(lambda i: \
            int(string[i:i+3]) % primes[i - 1] == 0, range(1,8))))

pandivs = list(filter(subStringDivisible, pandigitals))
pandivint = list(map(int,pandivs))
print(sum(pandivint))
