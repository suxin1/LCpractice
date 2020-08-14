"""
给一个用二维数组表示的图像，一个坐标(r, c)和整数n：
    1,选取与初始坐标(r, c)值相同的相邻坐标。斜角不算相邻。
    2,在面选择的坐标点重复上面的操作。
    3,需要将所有选择的坐标点的值改为新值n。
"""
from collections import deque


def switch_color(image, sr, sc, newColor):
    target = image[sr][sc]
    row = len(image)
    column = len(image[0])
    queue = deque([(sr, sc)])
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    visited = {}
    while queue:
        r, c = queue.popleft()
        image[r][c] = newColor
        visited[(r, c)] = True

        for direct in directions:
            nr, nc = r + direct[0], c + direct[1]
            if 0 <= nr < row and 0 <= nc < column and image[nr][nc] == target:
                if (nr, nc) not in visited:
                    queue.append((nr, nc))
    return image


a = [
    [1, 1, 1],
    [1, 1, 0],
    [1, 0, 1]
]

a2 = [
    [0, 0, 0],
    [0, 1, 1]
]
print(switch_color(a, 1, 1, 2))
