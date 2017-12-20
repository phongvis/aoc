'''https://nbviewer.jupyter.org/url/norvig.com/ipython/Advent%20of%20Code.ipynb'''
import re
from collections import Counter
import utils as ut

file = open('day09.txt')

# Part 1
def decompress(s):
    s = re.sub(r'\s', '', s)
    matcher = re.compile(r'[(](\d+)x(\d+)[)]').match

    'Traverse each character, if match the pattern, do the decompress, otherwise, advance one character'
    count = 0
    i = 0
    while i < len(s):
        m = matcher(s, i)
        if m:
            c, r = map(int, m.groups())
            i = m.end()
            count += r * decompress(s[i:i+c])
            i += c # update i
        else:
            count += 1
            i += 1
    return count

part1 = decompress(file.read())
print(part1)

# Part 2


part2 = ''
print(part2)