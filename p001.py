"""
Problem 1
---------
If we list all the natural numbers below 10 that are multiples of 3 or 5, we
get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""
MultipleOf3and5 = lambda num: num % 3 == 0 or num % 5 == 0
print(sum(filter(MultipleOf3and5, range(1000))))
