"""
给定一个 m × n 的二维网格，网格中有以下三种可能的初始化值：
-1 表示墙或是障碍物
0 表示一扇门
INF 无限表示一个空的房间。然后，我们用 231 - 1 = 2147483647 代表 INF。你可以认为通往门的距离总是小于 2147483647 的。
你要给每个空房间位上填上该房间到 最近 门的距离，如果无法到达门，则填 INF 即可。
"""

from queue import Queue
inf = 2147483647

import math
def walls_and_gates(rooms):
    if not len(rooms) or not len(rooms[0]):
        return
    m = len(rooms)
    n = len(rooms[0])
    
    directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    q = Queue()

    for i in range(len(rooms)):
        for j in range(len(rooms[i])):
            if rooms[i][j] != 0:
                continue
            q.put([i, j])
    
    while not q.empty():
        x, y = q.get()
        distance = rooms[x][y] + 1
        for direct in directions:
            nx = x + direct[0]
            ny = y + direct[1]
            if nx < 0 or nx >m or ny < 0 or ny > n or rooms[nx][ny] != inf:
                continue
            rooms[nx][ny] = distance
            q.put([nx, ny])

rooms = [
    [-1, -1, -1, -1, -1, -1, -1],
    [-1, inf, 0, inf, inf, inf, -1],
    [-1, inf, -1, inf, inf, inf, -1],
    [-1, inf, -1, inf, inf, inf, -1],
    [-1, inf, -1, inf, inf, inf, -1],
    [-1, inf, -1, inf, inf, inf, -1],
    [-1, -1, -1, -1, -1, -1, -1],
]

rooms_res = [
    [-1, -1, -1, -1, -1, -1, -1],
    [-1,  1,  0,  1,  2,  3, -1],
    [-1,  2, -1,  2,  3,  4, -1],
    [-1,  3, -1,  3,  4,  5, -1],
    [-1,  4, -1,  4,  5,  6, -1],
    [-1,  5, -1,  5,  6,  7, -1],
    [-1, -1, -1, -1, -1, -1, -1],
]

print(rooms)
walls_and_gates(rooms)
print(rooms)