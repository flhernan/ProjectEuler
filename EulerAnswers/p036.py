nums = list(filter( lambda num: str(num) == str(num)[::-1], range(1,1000000) ))
binary = lambda num: str(bin(num).replace('0b',''))
binaryPalindrome = lambda num: binary(num) == binary(num)[::-1]
result = list(filter( binaryPalindrome, nums))
print(sum(result))
