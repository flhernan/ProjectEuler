from itertools import combinations_with_replacement
from functools import reduce
from operator import add
side = list(range(1,1000))

filit = lambda pair: (pair[0]**2 + pair[1]**2)**.5 == (int)((pair[0]**2 + pair[1]**2)**.5)
sides = list(filter( filit, list(combinations_with_replacement(side, r=2))))
prod = lambda pair: (pair[0]**2 + pair[1]**2)**.5 + pair[0] + pair[1] < 1001
sidez = list(filter( prod, sides))
combs = lambda pair: [(pair[0]**2 + pair[1]**2)**.5,pair[0],pair[1]]
sidel = list(map( combs, sidez))

addall = lambda solution: solution[0] + solution[1] + solution[2]
result = list(map(addall, sidel))

numbers = list(set(result))

final = list(map( lambda num: [result.count(num),num], numbers))

print(max(final))


