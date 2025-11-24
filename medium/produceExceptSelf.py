# def productExceptSelf(nums: list[int]):
#     # res =[[] for i in range(len(nums))]
#     res = []
#     for i in range(len(nums)):
#         prod = 1
#         for j in range(len(nums)):
#             if i != j:
#                 prod *= nums[j]
#         res.append(prod)
#     return res


def productExceptSelf(nums: list[int]):
    prev = 1
    res = [0] * len(nums)
    for i in range(len(nums)):
        res[i] = prev
        prev *= nums[i]
    suff = 1
    for i in range(len(nums) - 1, -1, -1):
        res[i] *= suff
        suff *= nums[i]
    return res


print(productExceptSelf([1, 2, 4, 6]))
print(productExceptSelf([-1, 0, 1, 2, 3]))
