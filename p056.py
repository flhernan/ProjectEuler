sumDigits = lambda a: max(map(lambda b: sum(map(int,str(a**b))), range(1,100)))
digitalSum = list(map(sumDigits, range(1,100)))
print(max(digitalSum))
