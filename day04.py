import re
from collections import Counter
import utils as ut

def parse(line):
    'Return (name, sector, checksum) from aaaaa-bbb-z-y-x-123[abxyz]'
    return re.match(r'(.+)-(\d+)\[(.+)\]', line).groups()

def valid(name, checksum):
    counter = Counter(name.replace('-', ''))
    letters = sorted(counter, key = lambda k: (-counter[k], k))
    return checksum == ut.cat(letters[:5])

def decode(line):
    name, sector, checksum = parse(line)
    return int(sector) if valid(name, checksum) else 0

assert decode('aaaaa-bbb-z-y-x-123[abxyz]') == 123
file = open('day04.txt')
part1 = sum(map(decode, file))
print(part1)

# Part 2
def shift(text, n):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    n = n % len(alphabet)
    tr = str.maketrans(alphabet, alphabet[n:] + alphabet[:n])
    return text.translate(tr)

def decrypt(line):
    name, sector, _ = parse(line)
    return shift(name, int(sector)) + ' ' + sector

file = open('day04.txt')
for line in file:
    if re.search('north', decrypt(line)):
        print(line)

part2 = ''
print(part2)