with open("p022_names.txt", "r") as file:
  unsorted_names = file.read().replace('\"','').split(',')
  names = list(enumerate(sorted(unsorted_names), start = 1))

offset = ord('A') - 1
score = lambda name: name[0] * sum(map(lambda char: ord(char) - offset, name[1]))

print(sum(map(score,names)))
