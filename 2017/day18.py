import re
import itertools
from collections import Counter, defaultdict, deque

# Part 1
def solve(code, regs):
    def val(x):
        return regs[x] if x.isalpha() else int(x)

    pc = 0
    sound = 0
    while pc < len(code):
        op, x, y = tuple(code[pc])
        pc += 1

        if op == 'set':
            regs[x] = val(y)
        elif op == 'snd':
            sound = val(x)
        elif op == 'add':
            regs[x] += val(y)
        elif op == 'mul':
            regs[x] *= val(y)
        elif op == 'mod':
            regs[x] %= val(y)
        elif op == 'rcv':
            if val(x): break
        elif op == 'jgz':
            if val(x) > 0:
                pc += (val(y) - 1)

    return sound

def solve2(code):
    def val(x, i):
        return regs[i][x] if x.isalpha() else int(x)

    regs = [defaultdict(int), defaultdict(int)]

    pcs = [0, 0]
    idx = 0 # running program
    messages = [deque([]), deque([])]
    regs[1]['p'] = 1
    states = ['running', 'running']
    count = 0

    while True:
        op, x, y = tuple(code[pcs[idx]])
        pcs[idx] += 1
        currentPC = pcs[idx]
        states[idx] = 'running'

        if op == 'set':
            regs[idx][x] = val(y, idx)
        elif op == 'snd':
            messages[idx].append(val(x, idx))
            if idx == 1:
                count += 1
        elif op == 'add':
            regs[idx][x] += val(y, idx)
        elif op == 'mul':
            regs[idx][x] *= val(y, idx)
        elif op == 'mod':
            regs[idx][x] %= val(y, idx)
        elif op == 'rcv':
            other_idx = 1 - idx
            if messages[other_idx]: # If the other program has queuing messages, take it and continue
                regs[idx][x] = messages[other_idx].popleft()
            else: # switch
                if states[other_idx] == 'finish':
                    return count
                if not messages[idx] and states[other_idx] == 'waiting': # deadlock, nothing for you to wait
                    return count
                states[idx] = 'waiting'
                pcs[idx] -= 1
                currentPC = pcs[idx]
                idx = 1 - idx
        elif op == 'jgz':
            if val(x, idx) > 0:
                pcs[idx] += (val(y, idx) - 1)

        if currentPC >= len(code) or currentPC < 0:
            states[idx] == 'finish'

            # Switch
            idx = 1 - idx
            if states[idx] == 'finish' or states[idx] == 'waiting':
                return count

def parse(line):
    params = line.split()
    if len(params) == 2:
        params.append(None)
    return params

# part1 = solve(list(map(parse, open('vis/day18.txt').readlines())), defaultdict(int))
# print(part1)

# Part 2
part2 = solve2(list(map(parse, open('2017/day18.txt').readlines())))
print(part2)