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
