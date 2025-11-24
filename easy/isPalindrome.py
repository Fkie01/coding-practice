from audioop import reverse


def isPalindrome(s: str) -> bool:
    lower = s.lower()
    current_s = "".join([char for char in lower if char.isalnum()])
    return current_s == current_s[::-1]


s = "Was it a car or a cat I saw?"
s1 = "tab a cat"
print(isPalindrome(s))
print(isPalindrome(s1))
