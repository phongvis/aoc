import re
import itertools
from collections import Counter
import utils as ut

# Part 1
def filter(text):
    while True:
        newtext = text.replace('!!', '')
        if newtext == text:
            break
        text = newtext

    text = re.sub(r'!.', '', text)
    return text

def filter_garbage(text):
    return re.sub(r'<.*?>', '', filter(text))

def filter_commas(text):
    return re.sub(r',', '', text)

assert filter_garbage('<!!!>>') == ''
assert filter_garbage('<{o"i!a,<{i<a>') == ''
assert filter_garbage('') == ''
assert filter_garbage('<<<<>') == ''
assert filter_garbage('') == ''
assert filter_garbage('<{!>}>') == ''
assert filter_garbage('<!!>') == ''
assert filter_garbage('<!!!>>') == ''

def solve(text):
    text = filter_commas(filter_garbage(text))
    score = 0
    total_score = 0

    for c in text:
        if c == '{':
            score += 1
        elif c == '}':
            total_score += score
            score -= 1

    return total_score

def solve2(text):
    return sum(map(lambda x: len(x) - 2, re.findall(r'<.*?>', filter(text))))

print(solve('{}'))
print(solve('{{{}}}'))
print(solve('{<a>,<a>,<a>,<a>}'))
print(solve('{<{},{},{{}}>}'))
print(solve('{{<a>},{<a>},{<a>},{<a>}}'))
print(solve('{{<!>},{<!>},{<!>},{<a>}}'))

part1 = solve(ut.input(9).read())
print(part1)

# Part 2

part2 = solve2(ut.input(9).read())
print(part2)