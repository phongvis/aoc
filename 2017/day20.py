import re
import itertools
from collections import Counter, defaultdict
import utils as ut

# Part 1
def parse(line):
    nums = list(map(int, re.findall(r'([\-\d]+)', line)))
    return [nums[0:3], nums[3:6], nums[6:9]]

def update(p):
    p[1][0] += p[2][0]
    p[1][1] += p[2][1]
    p[1][2] += p[2][2]
    p[0][0] += p[1][0]
    p[0][1] += p[1][1]
    p[0][2] += p[1][2]

def dist(p):
    return abs(p[0][0]) + abs(p[0][1]) + abs(p[0][2])

def solve(file):
    ps = [parse(line) for line in file]

    for _ in range(1000):
        for p in ps:
            update(p)

    distances = list(map(dist, ps))
    return distances.index(min(distances))

def remove(ps):
    positions = defaultdict(list)
    for p in ps:
        t = tuple(p[0])
        positions[t].append(p)

    for v in positions.values():
        if len(v) > 1:
            for p in v:
                ps.remove(p)

def solve2(file):
    ps = [parse(line) for line in file]
    for _ in range(2000):
        for p in ps:
            update(p)
        remove(ps)

    return len(ps)

part2 = solve2(ut.input(20))
print(part2)