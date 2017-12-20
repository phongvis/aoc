'''https://nbviewer.jupyter.org/url/norvig.com/ipython/Advent%20of%20Code.ipynb'''
import re
from collections import Counter
import utils as ut

inp = 1350
goal = (31, 39)

# Part 1
def is_open(loc):
    x, y = loc
    num = x*x + 3*x + 2*x*y + y + y*y + inp
    return x >= 0 and y >= 0 and bin(num).count('1') % 2 == 0

def open_neighbors(loc):
    return filter(is_open, ut.neighbors4(loc))

def h(p):
    return ut.cityblock_distance(p, goal)

path = ut.Astar((1, 1), open_neighbors, h)
part1 = len(path) - 1
print(path)

# Part 2


part2 = ''
print(part2)