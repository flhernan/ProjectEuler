from functools import reduce
from operator import mul

indexes = [10**i for i in range(0,7)]
irrationalstr = '0.'+''.join(list(map( str, range(1, 1000001) )))

nums = list(map(lambda i: irrationalstr[i+1],indexes))
result = reduce(mul,list(map(int,nums)))
print(result)
