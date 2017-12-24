import re
import itertools
from collections import Counter, defaultdict, deque
import utils as ut

def parse(line):
    return sorted(list(map(int, line.split('/'))), reverse=False)

def check(p, path):
    for p2 in path:
        if p == p2 or p[::-1] == p2:
            return False
    return True

def find_bridges(start, parts):
    bridges = []

    def find_next(path, parts):
        for p in parts:
            if check(p, path):
                left_parts = parts.copy()
                left_parts.remove(p)

                if p[0] == path[-1][1]:
                    find_next(path + [p], left_parts)
                elif p[1] == path[-1][1]:
                    find_next(path + [p[::-1]], left_parts)

        # Couldn't find any port. Finish the bridge.
        bridges.append(path)

    find_next([start], parts)

    return bridges

def strength(b):
    return sum(map(lambda p: p[0] + p[1], b))

def solve(file):
    parts = list(map(parse, file))
    zero_parts = [p for p in parts if p[0] == 0]

    max_strength = 0
    max_length = 0
    longest_bridges = []
    bridges = []

    for p in zero_parts:
        bridges.extend(find_bridges(p, parts))

    for b in bridges:
        s = strength(b)
        if s > max_strength:
            max_bridge = b
            max_strength = s

        l = len(b)
        if l > max_length:
            max_length = l
            bridges = []
        if l == max_length:
            bridges.append(b)

    return max(map(strength, bridges))

print(solve(ut.input(24)))