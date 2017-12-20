import re
import numpy as np
from collections import Counter
import utils as ut

file = open('day08.txt')

# Part 1
def interpret(cmd, screen):
    a, b = map(int, re.findall(r'(\d+)', cmd))
    if cmd.startswith('rect'):
        screen[:b, :a] = 1
    elif cmd.startswith('rotate row'):
        screen[a, :] = rotate(screen[a, :], b)
    elif cmd.startswith('rotate col'):
        screen[:, a] = rotate(screen[:, a], b)

def rotate(items, n):
    return np.append(items[-n:], items[:-n])

def run(commands, screen):
    for cmd in commands:
        interpret(cmd, screen)
    return screen

screen = np.zeros((6, 50), dtype=np.int)
part1 = np.sum(run(file, screen))
print(part1)

# Part 2
for row in screen:
    print(ut.cat(' *'[pixel] for pixel in row))