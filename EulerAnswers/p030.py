
def splitNpower(number, power):
    stringN = str(number)
    return (number == sum(map(lambda N: int(N)**power,stringN)))

numbers = []
for i in range(2,1000000):
    if splitNpower(i, 5):
        numbers.append(i)
print(sum(numbers))
