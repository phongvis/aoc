import re
from collections import Counter
import hashlib
import utils as ut

door = 'abbhdwsy'

# Part 1
def find_password(door):
    max = 10 ** 9
    password = ''

    for i in range(max):
        t = bytes(door + str(i), 'utf-8')
        x = hashlib.md5(t).hexdigest()
        if x.startswith('00000'):
            password += x[5]
            print(i, x, password)
            if len(password) == 8:
                return password

# part1 = find_password(door)
# print(part1)

# Part 2
def find_password_2(door):
    max = 10 ** 9
    password = ['_'] * 8

    for i in range(max):
        t = bytes(door + str(i), 'utf-8')
        x = hashlib.md5(t).hexdigest()
        if x.startswith('00000'):
            idx = int(x[5], 16)
            if idx < 8 and password[idx] == '_':
                password[idx] = x[6]
                print(i, x, ''.join(password))
            if '_' not in password:
                return password

part2 = find_password_2(door)
# print(part2)