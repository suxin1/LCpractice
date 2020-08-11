"""
给定一个非负整数数组，a1, a2, ..., an, 和一个目标数，S。现在你有两个符号 + 和 -。
对于数组中的任意一个整数，你都可以从 + 或 -中选择一个符号添加在前面。
"""


# 动态规划
def sum_way(nums, S):
    mem = dict()
    length = len(nums)
    # 递推公式：
    #   recursion(index, rest) = recursion(index + 1, rest + nums[index]) + recursion(index + 1, rest - nums[index])

    def recursion(index, rest):
        key = str(index) + ',' + str(rest)
        if key in mem:
            return mem[key]

        # 当rest等于n（target）索引index等于列表长度时结束递归。
        if index == length:
            if rest == 0:
                return 1
            else:
                return 0

        result = recursion(index + 1, rest + nums[index]) + recursion(index + 1, rest - nums[index])

        mem[key] = result
        return result

    return recursion(0, S)


def sum_way_v2(nums, S):
    """
    把所有符号为正的数总和设为一个背包的容量，容量为x；把所有符号为负的数总和设为一个背包的容量，容量为y。
    在给定的数组中，有多少种选择方法让背包装满。令sum为数组的总和，则x+y = sum。
    而两个背包的差为S,则x-y=S。从而求得x=(S+sum)/2。
    """
    _sum = sum(nums)
    # 当 n + sum 不能被2除尽时，不满足上式。
    if S > _sum or (S + _sum) % 2 == 1:
        return 0

    value = int((S + _sum) / 2)

    dp = list([list([1 if j == 0 else 0 for j in range(value + 1)]) for i in range(len(nums) + 1)])  # 二维数组:i 表示前i个数，j：表示前i个数需要装满的容量
    # 前i个数装满j的方法    不考虑数i    考虑数i
    # dp[i][j]         = dp[i-1][j] + dp[i-1][j-nums[i-1]];
    print(dp)
    for i in range(1, len(nums) + 1):
        j = value
        while j > 0:
            if j >= nums[i - 1]:
                dp[i][j] = dp[i-1][j] + dp[i-1][j-nums[i-1]]
            else:
                dp[i][j] = dp[i-1][j]
            j -= 1
    print(dp)
    return dp[len(nums)][value]


array_t = [0, 0, 0, 0, 1]

print(sum_way_v2(array_t, 1))
