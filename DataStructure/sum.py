
def calculate_point(list):
    if not list:
        return 0
    list.sort()
    num_temp_sum = 1
    num_temp = list[0]
    sum = 0

    for i in range(1, len(list)):
        if list[i] != num_temp:
            sum += num_temp_sum ** 2
            num_temp_sum = 0
            num_temp = list[i]
        num_temp_sum += 1

    sum += num_temp_sum ** 2
    return sum

print(calculate_point([1,3,2,2,2,3,4,3,1]))
