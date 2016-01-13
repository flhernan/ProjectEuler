digit = lambda n: sorted(str(n))
properties = lambda n: digit(n) == digit(n*2) == digit(n*3) == digit(n*4) == digit(n*5) == digit(n*6)
number = list(filter(properties, range(100000, 1000000)))
print(number)
