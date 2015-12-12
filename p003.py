'''
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of this number?
'''
number = 600851475143

from eulerFunctions import isPrime

rootOfNumber = (int)(number**.5)
isFactor = lambda factor: ( number % factor == 0 )

factors = list(filter( isFactor, range(2, rootOfNumber) ))
print( max(filter( isPrime, factors )) )
