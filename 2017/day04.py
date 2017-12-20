import re
import itertools
from collections import Counter
import utils as ut

# Part 1
def valid(text):
    text = text.split()
    return len(set(text)) == len(text)

part1 = sum(map(valid, ut.input(4)))
print(part1)

# Part 2
def valid2(text):
    text = [''.join(sorted(t)) for t in text.split()]
    return len(set(text)) == len(text)

part2 = sum(map(valid2, ut.input(4)))
print(part2)