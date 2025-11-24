
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        fre = {}
        freq = [[] for i in range(len(nums) + 1)]
        
        for i in nums:
            fre[i] = 1 + fre.get(i, 0) 
        for key, value in fre.items():
            freq[value].append(key)

        res = []
        for i in range(len(freq) - 1, 0, -1):
            for j in freq[i]:
                res.append(j)
                if len(res) == k:
                    return res



        
