def maxArea(heights: list[int]) -> int:
    l = 0
    r = len(heights) - 1
    max_water = 0
    while l < r:
        # print(l)
        # print(r)
        bar_min = min(heights[l], heights[r])
        width = l - r
        # print(f"width {width}")
        current_water = (r - l) * bar_min
        max_water = max(max_water, current_water)
        if heights[l] < heights[r]:
            l += 1

        else:
            r -= 1

    return max_water


height = [1, 7, 2, 5, 4, 7, 3, 6]
height1 = [2, 2, 2]
print(maxArea(height))  # 36
print(maxArea(height1))  # 4
