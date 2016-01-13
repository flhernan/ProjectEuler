from math import sqrt
result = []
a = 1

def sum_of_divisors(number):
  factors = lambda divisors: number % divisors == 0
  return sum(filter(factors, range(1,(int)(number))))

while a<10000:
  b = sum_of_divisors(a)
  amicable = sum_of_divisors(b)
  
  if a!=b and a==amicable:
    result.append(a)
  a+=1

print sum(result)
