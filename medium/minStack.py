# Minimum Stack
# Solved
# Design a stack class that supports the push, pop, top, and getMin operations.

# MinStack() initializes the stack object.
# void push(int val) pushes the element val onto the stack.
# void pop() removes the element on the top of the stack.
# int top() gets the top element of the stack.
# int getMin() retrieves the minimum element in the stack.
# Each function should run in
# O
# (
# 1
# )
# O(1) time.

# Example 1:

# Input: ["MinStack", "push", 1, "push", 2, "push", 0, "getMin", "pop", "top", "getMin"]

# Output: [null,null,null,null,0,null,2,1]

# Explanation:
# MinStack minStack = new MinStack();
# minStack.push(1);
# minStack.push(2);
# minStack.push(0);
# minStack.getMin(); // return 0
# minStack.pop();
# minStack.top();    // return 2
# minStack.getMin(); // return 1
# Constraints:

# -2^31 <= val <= 2^31 - 1.
# pop, top and getMin will always be called on non-empty stacks.

### use the min_stack to save the accumulate min


class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.min_stack) == 0:
            self.min_stack.append(val)
        else:
            if self.min_stack[-1] >= val:
                self.min_stack.append(val)
            else:
                self.min_stack.append(self.min_stack[-1])

    def pop(self) -> None:
        n = len(self.stack)

        self.stack = self.stack[: n - 1]
        self.min_stack = self.min_stack[: n - 1]

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]

    def toString(self) -> None:
        for i in self.min_stack:
            print(f"string {i}")


s = MinStack()

s.push(0)
s.push(-1)
s.push(0)

# print()
# print(s.toString())
# print()
s.pop()

# print()
# print(s.toString())
# print()

print(s.getMin())
s.pop()
print(s.getMin())

# s.push(-2)
# s.push(-2)
# s.push(-3)
# s.push(-3)
# s.toString()
# print(s.getMin())
# print(s.pop())
# s.toString()
# print()
# print(s.getMin())
# print()
# print(s.getMin())
# print()
# s.pop()
# s.toString()
# print()
# print(s.top())


# print(s.getMin())
