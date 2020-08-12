"""
给定一个数N，使平方数(1, 4, 9, 16, ...)相加的和等于N，求最少要用多少个平方数。
# num_squares(n) = min{num_squares((n - k)) + 1 ||　ｋ属于任意平方数}
"""

from collections import deque
import math


# 粗暴求解
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


# num_squares(n) = min{num_squares((n - k)) + 1 ||　ｋ属于任意平方数}
# 粗暴求解算法2
def num_squares_v2(n: int) -> int:
    square_list = [(i + 1) ** 2 for i in range(int(math.sqrt(n)))]

    def minNumSquare(m):
        if m in square_list:
            return 1
        min_num = float('inf')
        for square in square_list:
            if square > m:
                break
            new_num = minNumSquare(m - square) + 1
            min_num = min(new_num, min_num)
        return min_num
    return minNumSquare(n)


# num_squares(n) = min{num_squares((n - k)) + 1 ||　ｋ属于任意平方数}
# 动态规划 (Dynamic programing)
# 从1求解最优解直到N
def num_squares_fast(n: int) -> int:
    square_list = [(i + 1) ** 2 for i in range(int(math.sqrt(n)))]

    dp = [float('inf')] * (n + 1)
    dp[0] = 0
    for i in range(1, n+1):
        for s in square_list:
            if i < s:
                break
            dp[i] = min(dp[i], dp[i-s] + 1)
    return dp[-1]


# 贪婪算法
def num_squares_greedy(n: int) -> int:
    num_squares = [(i + 1) ** 2 for i in range(int(math.sqrt(n)))]

    def is_divided_by(num: int, count: int) -> bool:
        if count == 1:
            return num in num_squares

        for k in num_squares:
            if is_divided_by(num - k, count - 1):
                return True
        return False

    for count in range(1, n+1):
        if is_divided_by(n, count):
            return count


print(num_squares_fast(7168))
