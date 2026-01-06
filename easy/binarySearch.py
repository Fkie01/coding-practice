def search(nums: list[int], target: int) -> int:
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = (right + left) // 2
        if nums[mid] == target:
            return mid

        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


nums = [-1, 0, 2, 4, 6, 8]
target = 4
print(search(nums, target))
nums = [-1, 0, 2, 4, 6, 8]
target = 3
print(search(nums, target))
