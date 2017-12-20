import re
import itertools
from collections import Counter, deque
import utils as ut

# Part 1
def parse(file):
    lookup = {}
    for line in file:
        nums = re.findall(r'(\d+)', line)
        lookup[nums[0]] = nums[1:]

    return lookup

def solve(lookup):
    frontier = deque(['0'])
    visited = set()

    while frontier:
        s = frontier.popleft()
        if s not in visited:
            visited.add(s)

            for s2 in lookup[s]:
                if s2 not in visited:
                    frontier.append(s2)

    return len(visited)

def solve2(lookup):
    left = set(lookup.keys())
    num_groups = 0

    while left:
        frontier = deque([left.pop()])
        num_groups += 1
        visited = set()

        while frontier:
            s = frontier.popleft()
            if s not in visited:
                visited.add(s)
                if s in left:
                    left.remove(s)

                for s2 in lookup[s]:
                    if s2 not in visited:
                        frontier.append(s2)

    return num_groups

part1 = solve(parse(ut.input(12)))
print(part1)

part2 = solve2(parse(ut.input(12)))
print(part2)