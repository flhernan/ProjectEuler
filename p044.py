from itertools import combinations
from functools import reduce
from operator import sub
from math import sqrt

pentagonalNums = list(map(lambda n: int(n*(3*n-1)/2), range(1,5000)))
pentagonalPairs = list(combinations(pentagonalNums, r=2))

def isPentagonal(num):
    a = (.5 + sqrt(.25 + 6*abs(num)))/3
    return a == (int)(a)
condition = lambda pair: isPentagonal(pair[0]+pair[1]) and\
        isPentagonal(pair[0]-pair[1])
resultPairs = list(filter( condition, pentagonalPairs))

D = list(map(lambda pair: abs(reduce(sub, pair)), resultPairs))
print(min(D))
