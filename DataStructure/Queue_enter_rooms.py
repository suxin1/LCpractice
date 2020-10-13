from typing import List
from collections import deque


def can_visit_all_rooms(rooms: List[List[int]]) -> bool:
    q = deque(rooms[0])
    visited = set()
    visited.add(0)

    while q:
        key = q.popleft()
        other_keys = rooms[key]
        visited.add(key)
        for k in other_keys:
            if k not in visited:
                q.append(k)

    return len(visited) == len(rooms)


print(can_visit_all_rooms([[1,3],[3,0,1, 2],[2],[0]]))
