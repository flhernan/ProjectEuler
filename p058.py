from eulerFunctions import splicePlaces, isPrime

def diags( ring ):
    if len(ring) == 1:
        return [1]
    end = ring[-1]
    diff = (int)(len(ring) / 4)
    return list(map(lambda n: end - n * diff, range(0,4)))

ratio = 1
index = 1
ring = [[1]]

totalPrimes = 1
diagonalPrimes = 0
lowerBound = 0
while ratio > .1:
    lowerBound = ring[-1][-1] + 1
    higherBound = lowerBound + index*8 + 1
    ring = splicePlaces( [index*8], list(range(lowerBound, higherBound)) )
    diagonals = diags(ring[-1])
    totalPrimes += len(diagonals)
    diagonalPrimes += len(list(filter(isPrime, diagonals)))
    ratio = diagonalPrimes / totalPrimes
    index += 1

print( index*2 - 1 )
