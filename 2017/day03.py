import re
import itertools
from collections import Counter, defaultdict
import utils as ut

# Part 1
n = 347991
def turn(dx, dy):
    return -dy, dx

def make_spirals(n):
    x, y = 0, 0 # starting location
    dx, dy = 1, 0 # right direction
    steps = 1
    current_step = 0
    twice = False

    for _ in range(n - 1):
        x += dx
        y += dy
        current_step += 1

        if current_step == steps:
            current_step = 0
            dx, dy = turn(dx, dy)

            if twice: steps += 1
            twice = not twice

    return x, y, abs(x) + abs(y)

part1 = make_spirals(n)
print(part1)

# Part 2
def sum_spirals(n):
    x, y = 0, 0 # starting location
    dx, dy = 1, 0 # right direction
    steps = 1
    current_step = 0
    twice = False
    values = defaultdict(int)
    values[(0, 0)] = 1

    while values[(x, y)] < n:
        x += dx
        y += dy
        current_step += 1

        values[(x, y)] = sum(values[p] for p in ut.neighbors8((x, y)))
        # print(x, y, values[(x, y)])

        if current_step == steps:
            current_step = 0
            dx, dy = turn(dx, dy)

            if twice: steps += 1
            twice = not twice

    return x, y, values[(x, y)]

part2 = sum_spirals(n)
print(part2)
