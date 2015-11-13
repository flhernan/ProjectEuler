'''
The prime factors of 13195 are 5, 7, 13 and 29.
'''
number = 600851475143
'''
What is the largest prime factor of this number?
'''
from eulerFunctions import isPrime
from math import sqrt

root_of_number = (int)(sqrt(number))
isFactor = lambda x: number%x==0
print(max([x for x in range(2,root_of_number) if isFactor(x) if isPrime(x)]))
