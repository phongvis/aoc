import re
import itertools
from collections import Counter
import utils as ut

# Part 1
def ga():
    a = 634
    while True:
        a *= 16807
        a %= 2147483647
        if a % 4 == 0:
            yield a

def gb():
    a = 301
    while True:
        a *= 48271
        a %= 2147483647
        if a % 8 == 0:
            yield a

def solve1():
    a = ga()
    b = gb()
    count = 0
    for i in range(5000000):
        if next(a) & 0xFFFF == next(b) & 0xFFFF:
            count += 1

    return count

part1 = solve1()
print(part1)

# Part 2

part2 = ''
print(part2)