from math import sqrt
from itertools import dropwhile

# .5n^2 + .5n - num
def isTriangular(num):
    a = .5
    b = .5
    c = -1 * num

    q1 = (-b + sqrt(b**2 - 4*a*c))/(2*a)
    return q1 == (int)(q1)

# 1.5n^2 - .5n - num
def isPentagonal(num):
    a = 1.5
    b = -.5
    c = -1 * num
    q1 = (-b + sqrt(b**2 - 4*a*c))/(2*a)
    return q1 == (int)(q1)

# 2n^2 - n - num
def isHexagonal(num):
    a = 2
    b = -1
    c = -1 * num

    q1 = (-b + sqrt(b**2 - 4*a*c))/(2*a)
    return q1 == (int)(q1)

isAll = lambda num: \
        isTriangular(num) and isPentagonal(num) and isHexagonal(num)

tph = list(filter(isAll, range( (int)(1*10**9), (int)(2*10**9) )))
print(tph[0])
