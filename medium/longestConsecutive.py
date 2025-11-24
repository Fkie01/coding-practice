def longestConsecutive(nums: list[int]) -> int:
    num_set = set(nums)
    longest = 0
    for i in nums:
        if (i - 1) not in num_set:
            length = 1
            while (i + length) in num_set:
                length += 1
            longest = max(longest, length)
    return longest


print(longestConsecutive([2, 20, 4, 10, 3, 4, 5]))
print(longestConsecutive([0, 3, 2, 5, 4, 6, 1, 1]))
