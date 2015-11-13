'''
By listing the first six prime numbers:
2, 3, 5, 7, 11, and 13,
we can see that the 6th prime is 13.

What is the 10 001st prime number?
'''
def getPrimesAt(index):
  primes = [2, 3]
  x = 3
  while(True):
    isPrime = True

    for y in primes:
      if x%y == 0:
        isPrime = False
        break

    if isPrime == True:
      primes.append(x)

    if index == len(primes):
      return primes

    x += 2
print(max(getPrimesAt(10001)))
