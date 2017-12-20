import re
import itertools as it
from collections import Counter
import utils as ut

# Part 1
def parse(line):
    return [int(x) for x in line.split()]

def diff(elements):
    return max(elements) - min(elements)

part1 = sum(diff(parse(line)) for line in ut.input(2))
print(part1)

# Part 2
def find(elements):
    return [b // a for a, b in it.combinations(sorted(elements), 2) if b % a == 0][0]

part2 = sum(find(parse(line)) for line in ut.input(2))
print(part2)