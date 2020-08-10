"""
给定一个非负整数数组，a1, a2, ..., an, 和一个目标数，S。现在你有两个符号 + 和 -。
对于数组中的任意一个整数，你都可以从 + 或 -中选择一个符号添加在前面。
"""


# 动态规划
def sum_way(nums, S):
    mem = dict()
    length = len(nums)

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


def sum_way_v2(l, n):
    """
    把所有符号为正的数总和设为一个背包的容量，容量为x；把所有符号为负的数总和设为一个背包的容量，容量为y。
    在给定的数组中，有多少种选择方法让背包装满。令sum为数组的总和，则x+y = sum。
    而两个背包的差为S,则x-y=S。从而求得x=(S+sum)/2。
    """
    _sum = sum(l)
    # 当 n + sum 不能被2除尽时，不满足上式。
    if n > _sum or (n + _sum) % 2 == 1:
        return 0

    value = int((n + _sum) / 2)
    dp = [0] * (value + 1)
    dp[0] = 1

    for num in l:
        rest = value
        while num <= rest:
            dp[rest] += dp[rest-num]
            rest -= 1

    return dp[value]


array_t = [1, 1, 1, 1, 1]
print(sum_way_v2(array_t, 3))
