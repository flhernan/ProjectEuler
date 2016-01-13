from itertools import combinations_with_replacement
n = 0
integers = []
while True:
    base = 0
    lastLen = len(integers)
    n += 1
    for base in range(1,1000):
        if len(str(base**n)) == n:
            integers.append(base**n)
    thisLen = len(integers)
    if thisLen - lastLen == 0:
        break
print(len(integers))






