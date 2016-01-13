from eulerFunctions import isPrime

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
