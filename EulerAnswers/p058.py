"""
Problem 58
----------
Starting with 1 and spiralling anticlockwise in the following way, a square
spiral with side length 7 is formed.

37 36 35 34 33 32 31
38 17 16 15 14 13 30
39 18  5  4  3 12 29
40 19  6  1  2 11 28
41 20  7  8  9 10 27
42 21 22 23 24 25 26
43 44 45 46 47 48 49

It is interesting to note that the odd squares lie along the bottom right
diagonal, but what is more interesting is that 8 out of the 13 numbers lying
along both diagonals are prime; that is, a ratio of 8/13 ≈ 62%.

If one complete new layer is wrapped around the spiral above, a square spiral
with side length 9 will be formed. If this process is continued, what is the
side length of the square spiral for which the ratio of primes along both
diagonals first falls below 10%?
"""
from math import sqrt
def splicePlaces( sliceSizes, listToSlice ):
    slicedUpList = []
    sliceBeginning = 0
    for sliceSize in sliceSizes:
        slicedUpList.append( listToSlice[ sliceBeginning : sliceBeginning + sliceSize  ] )
        sliceBeginning += sliceSize
    return slicedUpList

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

def diags( ring ):
    if len(ring) == 1:
        return [1]
    end = ring[-1]
    diff = (int)(len(ring) / 4)
    return list(map(lambda n: end - n * diff, range(0,4)))

ratio = 1
index = 1
ring = [[1]]

totalPrimes = 1
diagonalPrimes = 0
lowerBound = 0
while ratio > .1:
    lowerBound = ring[-1][-1] + 1
    higherBound = lowerBound + index*8 + 1
    ring = splicePlaces( [index*8], list(range(lowerBound, higherBound)) )
    diagonals = diags(ring[-1])
    totalPrimes += len(diagonals)
    diagonalPrimes += len(list(filter(isPrime, diagonals)))
    ratio = diagonalPrimes / totalPrimes
    index += 1

print( index*2 - 1 )
