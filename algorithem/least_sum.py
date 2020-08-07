"""
给一个数组l和一个整型数字n，找到一个l的子数组使其和大于等于n且长度最小。
"""

def least_sum(l, n):
    start = 0
    length = float("inf")
    sum = 0
    sub_array = []
    for i in range(len(l)):
        sum += l[i]
        while sum >= n:
            new_length = i - start + 1
            if new_length < length:
                length = new_length
                sub_array = l[start:i+1]
            sum -= l[start]
            start += 1
    return (length, sub_array)


a = [1, 3, 5, 3, 2, 6, 5, 4, 1, 3, 4]
print(least_sum(a, 1))
