from math import sqrt

def isPrime(num):
    if num == 2:
        return True

    if num % 2 == 0 or num < 2:
        return False

    i = 3
    sqrtOfNum = sqrt(num)

    while i <= sqrtOfNum:
        if num % i == 0:
            return False
        i = i+2

    return True

primes = list(filter( isPrime, range(10,1000000)))
def isTruncatableLeft(num):
    string = str(num)
    strNums = []
    while( len(string) > 0 ):
        strNums.append( int(string) )
        string = string[1:]
    return all(map( isPrime, strNums))

def isTruncatableRight(num):
    string = str(num)
    strNums = []
    while( len(string) > 0 ):
        strNums.append( int(string) )
        string = string[:-1]
    return all(map( isPrime, strNums))

elisa = lambda num: isTruncatableRight(num) and isTruncatableLeft(num)
lsa = list(filter( elisa, primes))
print(sum(lsa))
