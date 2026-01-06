def search(nums: list[int], target: int) -> int:
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        # print(mid)
        if nums[mid] == target:
            return mid
        if nums[left] <= nums[mid]:
            if nums[left] <= target and target <= nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if nums[mid] <= target and target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1

    return -1


nums = [3, 4, 5, 6, 1, 2]
target = 1
print(search(nums, target))
nums = [3, 5, 6, 0, 1, 2]
target = 4
print(search(nums, target))
nums = [5, 1, 2, 3, 4]
target = 1
print(search(nums, target))
nums = [1, 3]
target = 3
print(search(nums, target))
nums = [3, 1]
target = 3
print(search(nums, target))
nums = [3, 5, 1]
target = 3
print(search(nums, target))
nums = [5, 1, 3]
target = 5
print(search(nums, target))
