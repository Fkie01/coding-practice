# use dict to keep key of close parenthesis if incoming is close parenthesis then we will check with last element in stack to know that it close valid or not
# Valid Parentheses
# Solved
# You are given a string s consisting of the following characters: '(', ')', '{', '}', '[' and ']'.

# The input string s is valid if and only if:

# Every open bracket is closed by the same type of close bracket.
# Open brackets are closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
# Return true if s is a valid string, and false otherwise.

# Example 1:

# Input: s = "[]"

# Output: true
# Example 2:

# Input: s = "([{}])"

# Output: true
# Example 3:

# Input: s = "[(])"

# Output: false
# Explanation: The brackets are not closed in the correct order.

# Constraints:

# 1 <= s.length <= 1000
def isValid(s: str) -> bool:
    if len(s) % 2 != 0:
        return False

    stack = []
    check = {"]": "[", "}": "{", ")": "("}
    for c in s:
        if c in check:
            if stack and check[c] == stack[-1]:
                stack.pop()
                continue
            else:
                print("1")
                return False

        stack.append(c)

    if stack:
        print("2")
        return False
    return True


print(isValid("[]"))
print(isValid("([{}])"))
print(isValid("[(])"))
print(isValid("]]"))
print(isValid("(("))
print(isValid("()[]{}"))
