from itertools import permutations

with open('p059_cipher.txt','r') as encryptedFile:
    encrypted = encryptedFile.read().replace('\n','').split(',')

letters = list(map(lambda a: ''.join(a), list(permutations('abcdefghijklmnopqrstuvwxyz', r=3)) ))
key = ''
for letter in letters:
    cipher = encrypted.copy()
    for index in range(len(cipher)):
        cipher[index] = chr(int(cipher[index]) ^ ord(letter[index%3]))
        key = letter
    decrypted = ''.join(cipher)
    if ' the ' in decrypted:
        print(''.join(decrypted))
        print(key)
        decrypted = list(map(ord,decrypted))
        print(sum(decrypted))
        break

