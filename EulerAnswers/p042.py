from itertools import takewhile
from functools import reduce
from operator import add

with open('../EulerFiles/p042_words.txt','r') as wordFile:
    words = wordFile.read().replace('\"','').split(',')

maxWordLength = max(map( len, words))
maxTriangleNum = maxWordLength * 26

triangleNums = list(takewhile(lambda num: num < maxTriangleNum,\
                list(map( lambda n: (int)(.5*n*(n+1)), range(1,100)  ))))

alphabet = dict(zip('ABCDEFGHIJKLMNOPQRSTUVWXYZ', range(1,27)))

wordvalues = list(map( lambda word: \
        reduce( add, map( lambda letter: alphabet[letter], word)), words))

trianglewords = list(filter( lambda value: value in triangleNums, wordvalues ))
print(len(trianglewords))
