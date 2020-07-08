from typing import List
from collections import deque


def open_lock(target: str, deadends: List[str]) -> int:
    def neighbors(node):
        for i in range(4):
            m = int(node[i])
            for d in [1, -1]:
                y = (m + d) % 10
                yield node[:i] + str(y) + node[i + 1:]

    dead = set(deadends)
    queue = deque([('0000', 0)])
    visited = {'0000'}
    while queue:
        node, depth = queue.popleft()
        if node == target:
            return depth
        if node in dead:
            continue
        for neighbor in neighbors(node):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, depth + 1))
    return -1


step = open_lock("0202", ["0201", "0101", "0102", "1212", "2002"])
print(step)
