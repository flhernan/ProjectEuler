def cycle_count( number, current_remainder, remainders ):
    if (current_remainder == 0) or (number < 1):
        return len(remainders)

    while current_remainder < number:
        current_remainder *= 10

    current_remainder %= number

    if current_remainder in remainders:
        return len(remainders)
    else:
        remainders.append(current_remainder)
        return cycle_count(number, current_remainder, remainders)

get_cycle_count = lambda number: cycle_count(number, 1, [])
cycles = list(map( get_cycle_count, range(1000) ))
print(cycles.index( max(cycles) ))
