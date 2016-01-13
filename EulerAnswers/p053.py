from math import factorial as f
combination = lambda n: list(filter(lambda r: f(n)/(f(r)*f(n-r)) > 1000000, range(0, n)))
numOfCombinations = list(map( lambda num: len(combination(num)), range(1,101) ))
print(numOfCombinations)
print(sum(numOfCombinations))
