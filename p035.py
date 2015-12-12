from eulerFunctions import isPrime

primes = list(filter(isPrime,range(1,1000000)))

def isCircularPrime(num):
    string = str(num)
    liststr = [string]
    while len(liststr) < len(string):
        string = string[1:] + string[:1]
        liststr.append(string)
    nums = list(map(int,liststr))
    return all(map(isPrime,nums))

circularPrimes = list(filter(isCircularPrime,primes))
print(len(circularPrimes))
