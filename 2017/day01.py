import re
from collections import Counter
import utils as ut

file = open('2017/day01.txt').read()

# Part 1
def parse(s):
    s2 = s[1:] + s[:1]
    return sum(int(x[0]) for x in zip(s, s2) if x[0] == x[1])

assert parse('1122') == 3
assert parse('91212129') == 9
part1 = parse(file)
print(part1)

# Part 2
def parse_half(s):
    n = int(len(s) / 2)
    s2 = s[n:] + s[:n]
    return sum(int(x[0]) for x in zip(s, s2) if x[0] == x[1])

assert parse_half('1212') == 6
assert parse_half('123123') == 12

part2 = parse_half(file)
print(part2)
