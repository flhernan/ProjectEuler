ChainTo1 = [1]
ChainTo89 = [89]
def endOfChain(num):
    print(num)
    while True:
        if num in ChainTo1:
            break
        elif num in ChainTo89:
            break
        else:
            num = sum(map(lambda n: int(n)**2, str(num)))
    return num

startingNums = list(filter(lambda n: endOfChain(n) == 89, range(1,10000000) ))
print(len(startingNums))

