import re

file = open('day03.txt')
triangles = [parse_ints(l) for l in file]

def parse_ints(s):
    return [int(x) for x in re.findall(r'\d+', s)]

def is_triangle(sides):
    x, y, z = sorted(sides)
    return x + y > z

part1 = sum(map(is_triangle, triangles))
print(part1)

def transpose(matrix): return zip(*matrix)

def invert(triangles):
    list = []
    for i in range(0, len(triangles), 3):
        list.extend(transpose(triangles[i:i+3]))

    return list

part2 = sum(map(is_triangle, invert(triangles)))
print(part2)