'''
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?


NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.
'''


nums = list(range(1,21)) + list(range(30,101,10)) + [1000,1001]
words = ['one','two','three','four','five','six','seven',
         'eight','nine','ten','eleven','twelve','thirteen',
         'fourteen','fifteen','sixteen','seventeen','eighteen',
         'nineteen', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy',
         'eighty', 'ninety', 'hundred', 'onethousand', 'and']

my_dict = dict(zip(nums, words))
print(my_dict)

total_letters = 0

# one through nine appear 190 times each,
for i in range(1,10):
  total_letters += len(my_dict[i])*190

# ten through nineteen appear 10 times each,
for i in range(10,20):
  total_letters += len(my_dict[i])*10

# twenty, thirty...ninety appear 100 times each,
for i in range(20,91,10):
  total_letters += len(my_dict[i])*100

# hundred appears 900 times,
total_letters += len(my_dict[100])*900

# thousand appears one time,
total_letters += len(my_dict[1000])

# and appears 891 times.
total_letters += len(my_dict[1001])*891

print(total_letters)
