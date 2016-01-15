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
