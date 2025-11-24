

# Given an array of strings strs, group all anagrams together into sublists. You may return the output in any order.

# An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

# Example 1:

# Input: strs = ["act","pots","tops","cat","stop","hat"]

# Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]
# Example 2:

# Input: strs = ["x"]

# Output: [["x"]]
# Example 3:

# Input: strs = [""]

# Output: [[""]]
# Constraints:

# 1 <= strs.length <= 1000.
# 0 <= strs[i].length <= 100
# strs[i] is made up of lowercase English letters.


def groupAnagrams(strs: list[str]):
    if (len(strs) < 2):
        return [[strs[0]]] 
    anagrams = dict()
    for s in strs:
        keys = sorted(s)
        keys = ''.join(keys)
        if (keys not in anagrams):
            anagrams[keys] = [s]
        else:
            anagrams[keys].append(s)

    
    return list(anagrams.values())
    



print(groupAnagrams(["act","pots","tops","cat","stop","hat"]))  # [["hat"],["act", "cat"],["stop", "pots", "tops"]]
print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))  # [["bat"],["nat","tan"],["ate","eat","tea"]]
print(groupAnagrams([""]))  # [[""]]
print(groupAnagrams(["a"]))  # [["a"]]