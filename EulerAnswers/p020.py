from functools import reduce

def factorial(num):
  return reduce( (lambda x, y: x * y), range(1,num + 1) )

print( sum( map( int, str( factorial(100)))))
