import re
import itertools
from collections import Counter
import utils as ut

# Part 1
def solve(layers, delay):
    caughts = [d for d, r in layers.items() if (d + delay) % ((r - 1) * 2) == 0]

    # return sum(map(lambda c: layers[c] * c, caughts))
    return len(caughts)

def solve2(file):
    layers = { int(t[0]): int(t[1]) for t in [re.findall(r'(\d+)', line) for line in file] }

    delay = 0
    while True:
        if solve(layers, delay) == 0:
            return delay
        delay += 1

print(solve2(ut.input(13)))