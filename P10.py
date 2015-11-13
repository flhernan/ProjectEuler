'''
Problem 10

The sum of the primes below 10 is
2 + 3 + 5 + 7 = 17.

Find the sum of all the primes
below two million.
'''
def sumPrimes(maxnum):
  primes = [2]
  k = 1
  oner = 20001
  for i in range(3,maxnum,2):
    if i % oner == 0:
      print ("%s percent" % k)
      k += 1
      oner += 20000
    isPrime = True
    for j in primes:
      if i % j == 0:
        isPrime = False
        break
    if isPrime == True:
      primes.append(i)

  return(sum(primes))

print(sumPrimes(2000000))
