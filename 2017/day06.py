import re
import itertools
from collections import Counter
import utils as ut

# Part 1
def next(banks):
    max_value = max(banks)
    max_idx = banks.index(max_value)
    banks[max_idx] = 0

    for i in range(max_value):
        banks[(i + max_idx + 1) % len(banks)] += 1

    return banks

def solve(line):
    banks = [int(x) for x in line.split()]
    print(banks)
    states = dict()
    count = 0

    while tuple(banks) not in states:
        states[tuple(banks)] = count
        banks = next(banks)
        count += 1

    return count - states[tuple(banks)]

# part1 = solve('0 2 7 0')
part1 = solve('5	1	10	0	1	7	13	14	3	12	8	10	7	12	0	6')
print(part1)