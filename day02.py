import re
import utils as ut

keypad = """
.....
.123.
.456.
.789.
.....
""".split()

off = '.'

def move(c, x, y):
    if c == 'L' and keypad[x][y - 1] != off: y -= 1
    elif c == 'R' and keypad[x][y + 1] != off: y += 1
    elif c == 'U' and keypad[x - 1][y] != off: x -= 1
    elif c == 'D' and keypad[x + 1][y] != off: x += 1
    return x, y

def decode(ins, x=2, y=2):
    for line in ins:
        for c in line:
            x, y = move(c, x, y)
        yield keypad[x][y]

assert ut.cat(decode("ULL RRDDD LURDL UUUUD".split())) == '1985'

file = open('day02.txt')
part1 = ut.cat(decode(file))
print(part1)

# for line in file:

