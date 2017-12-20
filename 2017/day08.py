import re
import itertools
from collections import Counter, defaultdict
import utils as ut

# Part 1
def interpret(code, regs):
    "Execute instructions until pc goes off the end."
    maxreg = 0
    code = map(str.split, code)
    for inst in code:
        x, op, value, cond = inst[0], inst[1], int(inst[2]), 'regs[inst[4]] ' + inst[5] + ' ' + inst[6]

        if eval(cond):
            if op == 'inc': regs[x] += value
            elif op == 'dec': regs[x] -= value
            maxreg = max(maxreg, max(regs.values()))
    return maxreg

part1 = interpret(ut.input(8).readlines(), defaultdict(int))
print(part1)

# Part 2

part2 = ''
print(part2)