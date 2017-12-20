import re
import utils as ut

data = open('day01.txt').read()

loc = (0, 0)
face = 0 # N, E, S, W
steps = [(0, -1), (1, 0), (0, 1), (-1, 0)]

def move(face, loc, dir, step):
    offset = 1 if dir == 'R' else -1
    face = (face + offset) % 4
    loc = (loc[0] + steps[face][0] * step, loc[1] + steps[face][1] * step)
    return face, loc

ins = re.findall(r'(R|L)(\d+)', data)

for s in ins:
    face, loc = move(face, loc, s[0], int(s[1]))
part1 = abs(loc[0]) + abs(loc[1])
print(part1)

loc = (0, 0)
face = 0
visited = {loc}
part2 = None

def move2(face, loc, dir, step):
    offset = 1 if dir == 'R' else -1
    face = (face + offset) % 4
    for i in range(step):
        tmp_loc = (loc[0] + steps[face][0] * (i + 1), loc[1] + steps[face][1] * (i + 1))
        yield (face, tmp_loc)

for s in ins:
    small_steps = move2(face, loc, s[0], int(s[1]))
    for x in small_steps:
        print(x)
        face = x[0]
        loc = x[1]
        if loc in visited:
            part2 = abs(loc[0]) + abs(loc[1])
            break
        visited.add(loc)
    if part2 != None:
        break
print(part2)