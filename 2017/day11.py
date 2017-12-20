import re
import itertools
from collections import Counter
import utils as ut

# Part 1
dirs = {
    'n': (0, -1),
    's': (0, 1),
    'ne': (1, -1),
    'se': (1, 0),
    'nw': (-1, 0),
    'sw': (-1, 1)
}

def move(x, y, dir):
    return dirs[dir][0] + x, dirs[dir][1] + y

def dist(x, y):
    return (abs(x) + abs(y) + abs(x + y)) / 2

def solve(text):
    x, y = 0, 0
    max_steps = 0
    for dir in text.split(','):
        x, y = move(x, y, dir)
        max_steps = max(max_steps, dist(x, y))

    return dist(x, y)

print(solve('se,sw,se,sw,sw'))

part1 = solve(ut.input(11).read())
print(part1)

# Part 2

part2 = ''
print(part2)