'''
Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.


How many such routes are there through a 20×20 grid?
'''
from math import factorial

def square_lattice_path_combinations(side):
  total_paths = side*2
  f = factorial
  return( f(total_paths)/f(side)/f(total_paths-side) )


print(square_lattice_path_combinations(20))
