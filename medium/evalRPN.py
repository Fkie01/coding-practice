def evalRPN(tokens: list[str]) -> int:
    stack = []
    # operation = {"+": "sum", "-": "minus", "*": "mul", "/": "div"}
    for elem in tokens:
        if elem == "+":
            stack.append(stack.pop() + stack.pop())
        elif elem == "-":
            first = stack.pop()
            print(f"first {first}")
            second = stack.pop()
            print(f"second {second}")
            res = second - first
            stack.append(res)
        elif elem == "*":
            stack.append(stack.pop() * stack.pop())
        elif elem == "/":
            first = stack.pop()
            print(f"first {first}")
            second = stack.pop()
            print(f"second {second}")
            res = second / first
            stack.append(int(res))
        else:
            stack.append(int(elem))

        print(stack)
    return stack[0]


# tokens = ["1", "2", "+", "3", "*", "4", "-"]
tokens = ["4", "13", "5", "/", "+"]
print(evalRPN(tokens))
