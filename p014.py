'''
The following iterative sequence is defined
for the set of positive integers:

n -> n/2 (n is even)
n -> 3n + 1 (n is odd)

Using the rule above and starting with 13,
we generate the following sequence:

13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1
It can be seen that this sequence (starting
at 13 and finishing at 1) contains 10 terms.
Although it has not been proved yet (Collatz
Problem), it is thought that all starting
numbers finish at 1.

Which starting number, under one million,
produces the longest chain?

NOTE: Once the chain starts the terms are
allowed to go above one million.
'''
def maxCollatzChain(num):

  maxStartNum = 0
  maxlink = 0
  n = 2

  while(True):
    link = 1
    i = (int)(n)

    while(True):
      if i == 1:
        break
      elif i % 2 == 0:
        link+=1
        i = i/2
      else:
        link+=1
        i = 3*i+1

    if maxlink < link:
      maxlink = link
      maxStartNum = n

    if n % 10000==0:
      print ("%s percent"%(n/10000))

    if num == n:
      break

    n+=1
  return (maxStartNum)

print(maxCollatzChain(1000000))
