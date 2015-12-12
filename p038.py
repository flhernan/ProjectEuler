folo = lambda num: sorted(set(str(num))) == sorted(str(num))

fal = list(filter(folo,range(1,10000)))
nozeroes = lambda num: '0' not in str(num)
fal = list(filter(nozeroes,fal))

pds = []
for num in fal:
    string = str(num)
    pandigitalstr = string
    i = 2
    while len(pandigitalstr) < 9:
        nu = num *  i
        pandigitalstr += str(nu)
        i+=1
    if len(pandigitalstr) > 9:
        continue
    elif len(set(pandigitalstr)) == 9 and '0' not in pandigitalstr:
        pds.append(int(pandigitalstr))
    else:
        continue
print(max(pds))
