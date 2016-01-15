"""
A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
"""
from itertools import combinations_with_replacement
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

def isAbundant(num):
    if isPrime(num):
        return False
    factors = lambda factor: num % factor == 0
    biggest_factor = (int)(num/2) + 1
    sum_divisors = sum(filter( factors, range(1, biggest_factor) ))
    return sum_divisors > num

abundant_nums = list(filter( isAbundant, range(12, 28123) ))

abundant_pairs = list(combinations_with_replacement( abundant_nums, r=2))

sum_pairs = lambda pair: pair[0] + pair[1]
all_abundant_sums = list(set(map( sum_pairs, abundant_pairs )))

in_range = lambda num: num < 28123
abundant_sums = list(filter( in_range, all_abundant_sums ))

not_abundant_sum = lambda num: num not in abundant_sums
non_abundant_sums = list(filter( not_abundant_sum, range(1, 28123) ))
print( "non_abundant_sums: %d"% sum(non_abundant_sums))
