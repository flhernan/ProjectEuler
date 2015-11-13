'''
2**15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2**1000?
'''
def sum_of_digits(number):
  result = list(map(lambda x: int(x), list(str(number))))
  return(sum(result))

print(sum_of_digits(2**1000))
