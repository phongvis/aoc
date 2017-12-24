import re
import itertools
from collections import Counter, defaultdict, deque

# Part 1
def solve(code, regs):
    def val(x):
        return regs[x] if x.isalpha() else int(x)

    pc = 0
    count = 0

    while pc < len(code):
        op, x, y = tuple(code[pc])
        pc += 1

        if op == 'set':
            regs[x] = val(y)
        elif op == 'sub':
            regs[x] -= val(y)
        elif op == 'mul':
            regs[x] *= val(y)
            count += 1
        elif op == 'jnz':
            if val(x):
                pc += (val(y) - 1)

    return count

def parse(line):
    params = line.split()
    if len(params) == 2:
        params.append(None)
    return params

part1 = solve(list(map(parse, open('2017/day23.txt').readlines())), defaultdict(int))
print(part1)

def solve2():
    h = 0
    b = 84 * 100 + 100000
    c = b + 17000

    for x in range(b, c + 1, 17):
        for d in range(2, (int)(x**0.5)):
            if x % d == 0:
                h += 1
                break

    return h

print(solve2())