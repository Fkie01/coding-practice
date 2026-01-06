from typing import DefaultDict


def lengthOfLongestSubstring(s: str) -> int:
    map = DefaultDict(int)
    left = 0
    res = 0
    for r in range(len(s)):
        # print(f"l {left}")
        if s[r] in map:
            # print("in")
            left = max(map[s[r]] + 1, left)

        map[s[r]] = r

        res = max(r - left + 1, res)
    return res


s = "zxyzxyaz"
print(lengthOfLongestSubstring(s))
s = "xxxx"
print(lengthOfLongestSubstring(s))
s = "pwwkew"
print(lengthOfLongestSubstring(s))
s = "aabb"
print(lengthOfLongestSubstring(s))
s = ""
print(lengthOfLongestSubstring(s))
s = "dvdf"
print(lengthOfLongestSubstring(s))
