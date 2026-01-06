def trap(height: list[int]) -> int:
    l = 0
    max_l = 0
    res = 0
    block = 0
    while l < len(height) - 1:
        if height[l] > height[l+1]:



# height = [0, 2, 0, 3, 1, 0, 1, 3, 2, 1]
height = [0, 2, 0, 3]
print(trap(height))
