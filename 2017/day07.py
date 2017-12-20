import re
import itertools
from collections import Counter, defaultdict
import utils as ut

# Part 1
def parse(line):
    return re.findall(r'(\w+)', line)

def build_tree(text):
    nodes = dict()
    lines = [words for words in map(parse, text)]

    for words in lines:
        nodes[words[0]] = { 'name': words[0], 'weight': int(words[1]) }

    for words in lines:
        if (len(words) > 2):
            nodes[words[0]]['children'] = [nodes[x] for x in words[2:]]

    root = nodes['hmvwl']


    def compute_weight(node):
        if 'children' in node:
            for n in node['children']:
                node['weight'] += compute_weight(n)

        return node['weight']

    compute_weight(root)

    def printtree(node, indent=0):
        print('\t' * indent + node['name'] + ' ' + str(node['weight']))
        if 'children' in node:
            for n in node['children']:
                printtree(n, indent + 1)

    printtree(root)
    # non_leaf = set()
    # for word in count:
    #     if word not in leaf:
    #         non_leaf.add(word)

    # return count

def solve(file):
    return build_tree(file)

part1 = solve(ut.input(7))
print(part1)

# Part 2

part2 = ''
print(part2)