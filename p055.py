reverseAdd = lambda num: num + int(str(num)[::-1])
lychrelCheck = lambda num: str(num) == str(num)[::-1]

numOfLychrels = 0
for i in range(10000):
    lychrel = True
    number = i
    for j in range(50):
        number = reverseAdd(number)
        if lychrelCheck(number):
            lychrel = False
            break
    if lychrel == True:
        numOfLychrels += 1
print(numOfLychrels)

