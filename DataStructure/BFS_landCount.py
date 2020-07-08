from typing import List


def gen_id(x, y):
    return "row{}col{}".format(x, y)


def land_counter(grid: List[List[str]]) -> int:
    mem = {}
    count = 0
    directs = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    m = len(grid)
    if m == 0:
        return 0
    n = len(grid[0])
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 1 and not mem.get(gen_id(i, j)):
                q = []
                q.append([i, j])
                mem[gen_id(i, j)] = True
                count += 1
                while len(q):
                    x, y = q.pop()
                    for direct in directs:
                        nx = x + direct[0]
                        ny = y + direct[1]
                        # 排除超出边界何已经遍历过的节点。
                        if nx < 0 or nx >= m or ny < 0 or ny >= n: continue
                        if mem.get(gen_id(nx, ny)): continue
                        mem[gen_id(nx, ny)] = True
                        if grid[nx][ny] == 1: q.append([nx, ny])
    return count


def land_counter_v2(grid: List[List[str]]) -> int:
    if not grid:
        return 0
    count = 0
    m = len(grid)
    n = len(grid[0])

    def BFS(i, j):
        if grid[i][j] == 0:
            return
        grid[i][j] = 0
        if 0 <= i + 1 < m:
            BFS(i + 1, j)
        if 0 <= j + 1 < n:
            BFS(i, j + 1)
        if 0 <= i - 1 < m:
            BFS(i - 1, j)
        if 0 <= j - 1 < n:
            BFS(i, j - 1)

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 1:
                BFS(i, j)
                count += 1
    return count


land_map = [
    [1, 0, 0, 0, 0, 0],
    [1, 0, 0, 1, 0, 0],
    [1, 1, 0, 0, 0, 1],
    [1, 1, 0, 1, 0, 1],
    [1, 0, 0, 1, 1, 1],
    [1, 0, 0, 1, 1, 1],
]

land_map2 = [
    [1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0],
    [0, 0, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0],
    [0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
    [0, 0, 0, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 0],
    [0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1],
    [0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0],
    [1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0],
    [0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 0],
    [1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1],
    [0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0],
    [1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 1],
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0],
    [0, 1, 1, 0, 0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0, 0],
    [0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1],
    [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0]
]

land_num = land_counter_v2(land_map2)
print(land_num)
