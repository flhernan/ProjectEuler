'''
A Pythagorean triplet is a set of three
natural numbers, a < b < c, for which,

a**2 + b**2 = c**2
For example, 3**2 + 4**2 = 9 + 16 = 25 = 5**2.

There exists exactly one Pythagorean
triplet for which a + b + c = 1000.

Find the product abc.
'''
def PythagoreanProduct(num):
  for k in range(1,num-1):
    for j in range(1,k):
      for i in range(1,j):
        if i+j+k == num:
          if i**2 + j**2 == k**2:
            return i*j*k
print(PythagoreanProduct(1000))
