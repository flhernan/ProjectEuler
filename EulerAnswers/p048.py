selfpow = lambda n: n**n
selfPowResult = str(sum(list(map(selfpow,range(1,1001)))))
print(int(selfPowResult[-10:]))
