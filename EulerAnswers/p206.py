"""
Problem 206
-----------
Find the unique positive integer whose square has the form 1_2_3_4_5_6_7_8_9_0,
where each “_” is a single digit.
"""
from math import sqrt

minrange = (int)(sqrt(1020304050607080900))
maxrange = (int)(sqrt(1929394959697089990))
uniqueInteger = lambda num: str(num**2)[::2] == "1234567890"

number = max(filter(uniqueInteger, range(minrange, maxrange, 10)))

print(number)
