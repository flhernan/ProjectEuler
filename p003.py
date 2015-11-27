'''
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of this number?
'''
number = 600851475143

from eulerFunctions import isPrime
from math import sqrt

square_root = sqrt
root_of_number = (int)(square_root(number))
isFactor = lambda factor: ( number % factor == 0 )

factors = list(filter( isFactor, range(2, root_of_number) ))
largest_prime_factor = max(filter( isPrime, factors ))

print(largest_prime_factor)
