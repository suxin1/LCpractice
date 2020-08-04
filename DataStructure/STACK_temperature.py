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