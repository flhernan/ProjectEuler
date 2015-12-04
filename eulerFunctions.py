'''
isPrime: Function tests if a SMALL number is prime
@author: shay
'''
import math
def isPrime(number):
    if number == 2: return True
    if number % 2 == 0 or number <= 1: return False

    i = 3
    sqrtOfNumber = math.sqrt(number)

    while i <= sqrtOfNumber:
        if number % i == 0:
            return False
        i = i+2

    return True
'''
isPrimeLarge: Function tests if a LARGE number is prime using Fermat primality test
@author: shay
'''
import random

def isPrimeLarge(number):
  if number <= 1:
    return False
  for time in range(3):
    randomNumber = random.randint(2, number)-1
    if pow(randomNumber, number-1, number)!=1:
        return False
  return True
"""
splicePlaces in Haskell:

slice from to = (take (to - from)).(drop from)

splitAts xs [] = []
splitAts [] xs = []
splitAts (n:ns) xs = take n xs : splitAts ns (drop n xs)

Got this from my buddy, Dan! He's great! Hire him!
"""

#Splice places in Python:
def splicePlaces( sliceSizes, listToSlice ):
    slicedUpList = []
    sliceBeginning = 0
    for sliceSize in sliceSizes:
        slicedUpList.append( listToSlice[ sliceBeginning : sliceBeginning + sliceSize  ] )
        sliceBeginning += sliceSize
    return slicedUpList

