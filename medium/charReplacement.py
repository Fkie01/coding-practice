from typing import DefaultDict


def characterReplacement(s: str, k: int) -> int:
    res = 0
    map = DefaultDict(int)
    mostFreq = 0
    left = 0
    for r in range(len(s)):
        map[s[r]] = map.get(s[r], 0) + 1
        mostFreq = max(mostFreq, map[s[r]])
        # print(f"most{mostFreq}")
        # print(f"left{left}")
        # print(f"r{r}")
        while (r - left + 1) - mostFreq > k:
            # print(f"inner left{left}")
            map[s[left]] -= 1
            left += 1
        res = max(res, r - left + 1)
        # print(f"res{res}")
    return res


s = "XYYX"
k = 2
print(characterReplacement(s, k))
s = "AAABABB"
k = 1
print(characterReplacement(s, k))
s = "ABAB"
k = 2
print(characterReplacement(s, k))
s = "ABAA"
k = 0
print(characterReplacement(s, k))
