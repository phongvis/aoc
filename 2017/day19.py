import utils as ut

def solve(file):
    grid = file.read().splitlines()
    y = 0
    x = grid[0].index('|')
    dir = 'd'
    labels = []
    steps = 0

    while True:
        c = grid[y][x]

        if c == ' ':
            break

        if c.isalpha():
            labels.append(c)

        if c == '+':
            if dir in 'ud':
                if grid[y][x-1] != ' ': dir = 'l'
                if grid[y][x+1] != ' ': dir = 'r'
            else:
                if grid[y-1][x] != ' ': dir = 'u'
                if grid[y+1][x] != ' ': dir = 'd'

        if dir == 'u': y -= 1
        if dir == 'd': y += 1
        if dir == 'l': x -= 1
        if dir == 'r': x += 1

        steps += 1

#         print(c, dir)

    print(''.join(labels))
    print(steps)

solve(ut.input(19))