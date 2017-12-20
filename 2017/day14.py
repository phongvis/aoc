from collections import deque
import utils as ut
import day10

key = 'oundnydw'

def get_row(i):
    k = day10.solve2(range(256), '{}-{}'.format(key, i))
    binhash = bin(int(k, 16))[2:].zfill(128)
    return list(map(int, binhash))

def solve():
    grid = list(map(get_row, range(128)))
    seen = set()

    def dfs(i, j):
        if not grid[i][j]: return
        if (i, j) in seen: return

        seen.add((i, j))

        if i > 0: dfs(i - 1, j)
        if i < 127: dfs(i + 1, j)
        if j > 0: dfs(i, j - 1)
        if j < 127: dfs(i, j + 1)

    def bfs(i, j):
        frontier = deque([(i, j)])
        seen.add((i, j))
        while frontier:
            c = frontier.popleft()
            for p in ut.neighbors4(c):
                if p in seen: continue

                if p[0] >= 0 and p[0] < 128 and p[1] >= 0 and p[1] < 128 and grid[p[0]][p[1]]:
                    frontier.append(p)
                    seen.add(p)

    count = 0

    for i in range(128):
        for j in range(128):
            if not grid[i][j] or (i, j) in seen: continue

            count += 1
            bfs(i,j)
            # dfs(i, j)

    print(count)

solve()