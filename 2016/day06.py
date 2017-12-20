import re
from collections import Counter
import utils as ut

file = open('day06.txt')

# Part 1
counts = [Counter(x) for x in ut.transpose(file.read().split())]
part1 = ut.cat([c.most_common(1)[0][0] for c in counts])
print(part1)

# Part 2
part2 = ut.cat([c.most_common()[-1][0] for c in counts])
print(part2)