fibonacci = [1,1]
while len(str( fibonacci[-1] )) != 1000:
    fibonacci.append( fibonacci[-2] + fibonacci[-1] )

print( fibonacci.index(fibonacci[-1]) + 1 )

