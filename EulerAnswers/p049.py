from itertools import permutations, combinations_with_replacement, combinations
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

comboes = list(map(lambda comboes: ''.join(comboes), combinations_with_replacement('123456789', r=4)))

permslist = list(map(lambda perms: list(map(lambda p: int(''.join(p)), perms)), list(map(lambda c: list(permutations(c, 4)), comboes)) ))

primeperms = list(map(lambda perm: sorted(set(filter( lambda p: isPrime(int(p)) ,perm))), permslist))

combomaker = lambda listl: list(combinations(listl,r=3))
sequence = lambda pair: pair[2] - pair[1] == pair[1] - pair[0] and pair[2] - pair[1] != 0
arithmetic = lambda listl: list(filter( sequence, combomaker(listl) ))
combobreaker = list(map( arithmetic, primeperms))
while [] in combobreaker: combobreaker.remove([])

stringy = lambda lstl: int(str(lstl[0][0]) + str(lstl[0][1]) + str(lstl[0][2]))
concatenatedSequence = list(map( stringy, combobreaker ))
print(concatenatedSequence[1])
