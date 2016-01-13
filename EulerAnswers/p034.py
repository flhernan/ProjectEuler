from math import factorial as f
stringNum = list(map(str,range(10,100000)))
facts = list(filter(lambda n: sum(map(lambda l: f(int(l)),n)) == int(n), stringNum))
facts = list(map(int, facts))
print(sum(facts))
