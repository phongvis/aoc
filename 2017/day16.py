import re
import itertools
from collections import Counter
import utils as ut

# Part 1
def spin(p, n):
    return p[-n:] + p[:-n]

def swap(p, x, y):
    x, y = min(x, y), max(x, y)
    return p[:x] + p[y] + p[x+1:y] + p[x] + p[y+1:]

def partner(p, x, y):
    return swap(p, p.find(x), p.find(y))

def dance(program, ins):
    for t in ins:
        if t[0] == 's':
            program = spin(program, int(t[1:]))
        if t[0] == 'x':
            t = t[1:].split('/')
            program = swap(program, int(t[0]), int(t[1]))
        if t[0] == 'p':
            t = t[1:].split('/')
            program = partner(program, t[0], t[1])

    return program

def solve(text, size):
    p0 = program = ''.join(chr(97 + i) for i in range(size))
    ins = text.split(',')
    cycle_length = 0

    for i in range(1000000000):
        program = dance(program, ins)
        if program == p0:
            cycle_length = i + 1
            break

    for i in range(1000000000 % cycle_length):
        program = dance(program, ins)

    return program

part1 = solve(ut.input(16).read(), 16)
print(part1)

# Part 2

part2 = ''
print(part2)