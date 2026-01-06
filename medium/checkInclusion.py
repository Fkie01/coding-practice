from typing import DefaultDict


def checkInclusion(s1: str, s2: str) -> bool:
    if len(s1) > len(s2):
        return False
    s1_dict = DefaultDict(int)
    for s in s1:
        s1_dict[s] = s1_dict.get(s, 0) + 1

    for i in range(0, len(s2) - len(s1) + 1):
        print(i)
        dump = DefaultDict(int)
        for j in range(i, i + len(s1)):
            dump[s2[j]] = dump.get(s2[j], 0) + 1
        if dump == s1_dict:
            return True
    return False


s1 = "abc"
s2 = "lecabee"
print(checkInclusion(s1, s2))
s1 = "abc"
s2 = "lecaabee"
print(checkInclusion(s1, s2))
s1 = "adc"
s2 = "dcda"
print(checkInclusion(s1, s2))
