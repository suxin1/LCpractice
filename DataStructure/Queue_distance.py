from queue import Queue
from typing import List


def distance_counting(matrix: List[List[int]]) -> List[List[int]]:
    row = len(matrix)
    column = len(matrix[0])
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    q = Queue()
    visited = set()

    for i in range(row):
        for j in range(column):
            if matrix[i][j] == 0:
                q.put((i, j))
                visited.add((i, j))

    while not q.empty():
        r, c = q.get()
        distance = matrix[r][c] + 1
        for direct in directions:
            dr, dc = direct
            nr, nc = r + dr, c + dc
            if nr < 0 or nr >= row or nc < 0 or nc >= column or (nr, nc) in visited:
                continue
            visited.add((nr, nc))
            matrix[nr][nc] = distance
            q.put((nr, nc))

    return matrix


mt = [
    [0, 0, 0],
    [0, 1, 0],
    [1, 1, 1]
]

print(distance_counting(mt))

# 字符串求和
def multiply(num1: str, num2: str) -> str:
    n = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9}
    num1_len = len(num1) - 1
    num2_len = len(num2) - 1

    sum = 0
    for i in range(len(num1)):
        for j in range(len(num2)):
            sub_s = n[num1[i]] * (10 ** (num1_len - i)) * n[num2[j]] * (10 ** (num2_len - j))
            sum += sub_s
    return str(sum)


print(multiply("123", "456"))