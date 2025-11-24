def threeSum(nums: list[int]) -> list[list[int]]:
    res = []
    nums.sort()
    # print(nums)
    for i in range(len(nums)):
        if nums[i] > 0:
            break
        if i > 0 and nums[i - 1] == nums[i]:
            continue

        l = i + 1
        r = len(nums) - 1
        # dummy = set()
        while l < r:
            target = nums[i] + nums[l] + nums[r]
            print(f"l {nums[l]}")
            print(f"r {nums[r]}")
            print(target)
            if target < 0:
                l += 1
            elif target > 0:
                r -= 1
            else:
                res.append([nums[i], nums[l], nums[r]])
                r -= 1
                l += 1
                while nums[l] == nums[l - 1] and l < r:
                    l += 1

    return res


nums = [-1, 0, 1, 2, -1, -4]  # [[-1,-1,2],[-1,0,1]]
nums1 = [0, 1, 1]  # []
nums2 = [0, 0, 0, 0]  # [[0,0,0]]
nums3 = [1, -1, -1, 0]  # [[-1,0,1]]
print(threeSum(nums))
print(threeSum(nums1))
print(threeSum(nums2))
print(threeSum(nums3))
