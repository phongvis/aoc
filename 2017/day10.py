import re
import itertools
from collections import Counter
import utils as ut

# Part 1
def next(seq, pos, size):
    end_idx = pos + size
    if end_idx <= len(seq):
        rev = list(reversed(seq[pos:end_idx]))
        seq = list(seq[:pos]) + list(rev[:]) + list(seq[end_idx:])
    else:
        end_idx2 = size - (len(seq) - pos)
        part2_size = len(seq) - pos
        rev = list(reversed(seq[pos:] + seq[:end_idx2]))
        seq = list(rev[part2_size:]) + list(seq[end_idx2:pos]) + list(rev[:part2_size])

    return seq

def solve(seq, lengths):
    pos = 0
    for i in range(len(lengths)):
        seq = next(seq, pos, lengths[i])
        pos = (pos + lengths[i] + i) % len(seq)

    return seq[0] * seq[1]

def hash(seq):
    nums = []
    for i in range(16):
        r = seq[i * 16: (i + 1) * 16]
        ans = 0
        for j in range(16):
           ans = ans ^ r[j]
        nums.append(ans)

    return ''.join(map(dense, nums))

def dense(n):
    h = hex(n)[2:]
    return h if len(h) == 2 else '0' + h

def solve2(seq, lengths):
    lengths = list(map(lambda x: ord(x), lengths))
    lengths.extend([17, 31, 73, 47, 23])
    n = len(lengths)
    pos = 0

    for i in range(64):
        for j in range(n):
            seq = next(seq, pos, lengths[j])
            pos = (pos + lengths[j] + i * n + j) % len(seq)

    return hash(seq)

# part1 = solve(range(256), [225,171,131,2,35,5,0,13,1,246,54,97,255,98,254,110])
# print(part1)
# Part 2

part2 = solve2(range(256), '225,171,131,2,35,5,0,13,1,246,54,97,255,98,254,110')
print(part2)