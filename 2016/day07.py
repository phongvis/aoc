import re
from collections import Counter
import utils as ut

file = open('day07.txt')

# Part 1
def abba(s):
    return any(a == d != b == c for (a, b, c, d) in subsequences(s, 4))

def subsequences(s, n):
    return [s[i:i + n] for i in range(len(s) + 1 - n)]

def segment(line):
    return re.split(r'\[|\]', line)

def tls(segments):
    outsides = segments[0::2]
    insides = segments[1::2]
    return any(map(abba, outsides)) and not any(map(abba, insides))

part1 = sum(tls(segment(line)) for line in file)
print(part1)

# Part 2
alphabet = 'abcdefghijklmnopqrstuvwxyz'

def ssl(segments):
    "Is there an ABA outside brackets, and the corresponding BAB inside?"
    outsides = '###'.join(segments[0::2])
    insides = '###'.join(segments[1::2])
    return any(a+b+a in outsides and b+a+b in insides for a in alphabet for b in alphabet if a != b)

file = open('day07.txt')
part2 = sum(ssl(segment(line)) for line in file)
print(part2)
