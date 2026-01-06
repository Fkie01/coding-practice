def findDuplicate(nums: list[int]) -> int:
    size = len(nums)
    slow, fast = 0, 0
    while True:
        ele1 = nums[slow % size]
        ele2 = nums[fast % size]
        if ele1 == ele2 and slow != fast:
            break
        slow += 1
        fast += 2
    return ele1


nums = [1, 2, 3, 2, 2]
print(findDuplicate(nums))
nums = [1, 2, 3, 4, 4]
print(findDuplicate(nums))
nums = [1, 2, 3, 3]
print(findDuplicate(nums))
nums = [3, 3]
print(findDuplicate(nums))
