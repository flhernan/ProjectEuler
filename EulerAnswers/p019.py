month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
sundays = 0
starting_day = (sum(month_days) + 1)% 7
print(starting_day)
year = 1901

#1 jan 1901 is a wednesday
while year != 2001:
  for i in month_days:
    if (year % 4 == 0) and (i == 28):
      starting_day += 1
    starting_day = (starting_day + i) % 7
    if starting_day == 0:
      sundays += 1
  year += 1
print(sundays)

