"""
 * 根据每日 气温 列表，重新生成一个列表。对应位置的输出为：要想观测到更高的气温，至少需要等待的天数。如果气温在这之后都不会升高，请在该位置用 0 来代替。
 * 解决方法：
 *     1.维护一个单调栈，这个栈储存需要观测的温度索引。遍历温度列表，如果栈为空则将其推进栈中。
 *     2.如果当前温度T[i] > 栈中顶部索引温度T[prev_index], 移除顶部索引 prev_index，算出 answer[prev_index] = i - prev_index。重复此步骤，直到栈为空。
"""
from typing import List


def daily_temperature(T: List[int]) -> List[int]:
    res = []
    for i in range(len(T)):

        sum = 0
        last = 0
        for j in range(i+1, len(T)):
            sum += 1
            if T[j] > T[i]:
                last = T[j]
                break

        if last > T[i]:
            res.append(sum)
        else:
            res.append(0)
    return res


def daily_temperature_stack(T: List[int]) -> List[int]:
    res = [0] * len(T)
    stack = []
    for i in range(len(T)):
        while stack and T[i] > T[stack[-1]]:
            prev_index = stack.pop()
            res[prev_index] = i - prev_index
        stack.append(i)

    return res


temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
print(daily_temperature_stack(temperatures))