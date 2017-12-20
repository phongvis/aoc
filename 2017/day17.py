import re
import itertools
from collections import Counter
import utils as ut

# Part 1
def move(buff, idx, step, value):
    idx = (idx + step) % len(buff)
    buff.insert(idx+1, value)
    return buff, idx+1

def solve(step):
    buff = [0]
    idx = 0
    for i in range(2017):
        buff, idx = move(buff, idx, step, i + 1)
    return buff[idx+1]

def solve2(step):
    buff = [0]
    idx = 0
    next_num = 0
    for i in range(1, 50000001):
        idx = (idx + step) % i
        if idx == 0:
            next_num = i + 1
        idx += 1

    return next_num
# part1 = solve(382)
# print(part1)
part2 = solve2(382)
print(part2)