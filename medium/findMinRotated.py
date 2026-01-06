def findMin(nums: list[int]) -> int:
    left = 0
    right = len(nums) - 1
    most_min = 1_001
    while left <= right:
        mid = (left + right) // 2
        current_min = nums[mid]
        # print(current_min)
        if current_min < most_min:
            most_min = current_min
        if current_min > nums[right]:
            left = mid + 1
        elif current_min <= nums[right]:
            right = mid - 1

    return most_min


# nums = [3, 4, 5, 6, 1, 2]
# nums = [4, 5, 0, 1, 2, 3]

# nums = [4, 5, 6, 7]
# nums = [2, 3, 4, 5, 1]
# nums = [5, 1, 2, 3, 4]
nums = [3, 4, 5, 1, 2]
print(findMin(nums))
