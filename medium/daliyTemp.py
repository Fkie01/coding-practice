def dailyTemperatures(temperatures: list[int]) -> list[int]:
    n = len(temperatures)
    res = [0 for i in range(n)]
    stack = []  # (temp, id)
    for i in range(n):
        temp = temperatures[i]
        # print(temp)
        while stack and stack[-1][0] < temp:
            temp_new, id = stack.pop()
            res[id] = i - id

        stack.append((temp, i))
        # print(stack)
    return res


temperatures = [34, 80, 80, 80, 34, 80, 80, 80, 34, 34]  # [1,0,0,0,1,0,0,0,0,0]
# temperatures = [30, 38, 30, 36, 35, 40, 28]  # [1,4,1,2,1,0,0]
print(dailyTemperatures(temperatures))
