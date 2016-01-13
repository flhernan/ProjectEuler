with open('p079_keylog.txt','r') as keylogFile:
    keylog = keylogFile.read().split('\n')
    keylog.pop()

passcode = list('01236789')
for key in keylog:
    middle = key[1]
    left = key[0]
    right = key[2]

    i1 = passcode.index(middle)
    i2 = passcode.index(left)
    i3 = passcode.index(right)

    if i1 < i2:
        passcode[i1] = left
        passcode[i2] = middle

    elif i1 > i3:
        passcode[i1] = right
        passcode[i3] = middle

print(int(''.join(passcode)))
