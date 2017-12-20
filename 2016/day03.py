import re
import utils as ut

file = open('day03.txt')

def parse_ints(s):
    return [int(x) for x in re.findall(r'\d+', s)]

triangles = [parse_ints(l) for l in file]

def is_triangle(sides):
    x, y, z = sorted(sides)
    return x + y > z

part1 = sum(map(is_triangle, triangles))
print(part1)

def invert(triangles):
    for i in range(0, len(triangles), 3):
        yield from ut.transpose(triangles[i:i+3])

part2 = sum(map(is_triangle, invert(triangles)))
print(part2)