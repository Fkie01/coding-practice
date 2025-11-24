# Encode and Decode Strings
# Solved
# Design an algorithm to encode a list of strings to a single string. The encoded string is then decoded back to the original list of strings.

# Please implement encode and decode

# Example 1:

# Input: ["neet","code","love","you"]

# Output:["neet","code","love","you"]
# Example 2:

# Input: ["we","say",":","yes"]

# Output: ["we","say",":","yes"]
# Constraints:

# 0 <= strs.length < 100
# 0 <= strs[i].length < 200
# strs[i] contains only UTF-8 characters.


def encode(strs: list[str]) -> str:
    res = ""
    for s in strs:
        res += str(len(s)) + "#" + s
    return res


def decode(s: str) -> list[str]:
    res = []
    count = 0
    total = 0
    while count < len(s):
        while s[count + total] != "#":
            # count += 1
            total += 1
        # print(f"total {total}")
        word_len = int(s[count : count + total])
        print(word_len)
        word = s[count + 1 + total : count + 1 + total + word_len]
        res.append(word)
        count += 1 + total + word_len
        total = 0
    return res


# print(encode(["hello", "world", "123"]))
# print(decode("5#hello5#world3#123"))

# print(encode(["we", "say", ":", "yes", "!@#$%^&*()"]))
# print(decode("2#we3#say1#:3#yes10#!@#$%^&*()"))


print(
    encode(
        [
            "The quick brown fox",
            "jumps over the",
            "lazy dog",
            "1234567890",
            "abcdefghijklmnopqrstuvwxyz",
        ]
    )
)
print(
    decode(
        "19#The quick brown fox14#jumps over the8#lazy dog10#123456789026#abcdefghijklmnopqrstuvwxyz"
    )
)
