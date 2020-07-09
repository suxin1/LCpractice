from collections import deque
import math


def numSquares(n: int) -> int:
    squareList = [(i + 1) ** 2 for i in range(int(math.sqrt(n)))]
    squareList.reverse()
    q = deque()
    for s in squareList:
        q.append((s, 1))
    while q:
        sum, count = q.popleft()
        if sum == n:
            return count
        if sum > n:
            continue

        for s in squareList:
            q.append((sum + s, count + 1))

    return -1

print(numSquares(7168))