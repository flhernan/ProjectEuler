from eulerFunctions import splicePlaces

ringCount = 500
index = range(8, ringCount*8 + 1, 8)
rings = splicePlaces(index, list(range(2, 2000000)))
rings.reverse()
rings.append([1])
rings.reverse()

def diags( ring ):
    if len(ring) == 1:
        return [1]
    end = ring[-1]
    diff = (int)(len(ring) / 4)
    return list(map(lambda n: end - n * diff, range(0,4)))

result = list(map(lambda ring: diags(ring), rings))
print( sum(map(lambda diags: sum(diags), result)) )
