import re
import itertools
from collections import Counter
import utils as ut

# Part 1
def solve(code):
    pc = 0
    steps = 0
    while pc < len(code):
        oldpc = pc
        pc += code[pc] # jump
        # code[oldpc] += 1 # inc
        code[oldpc] += (-1 if code[oldpc] >= 3 else 1) # inc
        # print(code)
        steps += 1
    return steps

code = [int(x) for x in ut.input(5)]
part1 = solve(code)
print(part1)