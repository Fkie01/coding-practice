def carFleet(target: int, position: list[int], speed: list[int]) -> int:
    car = [[pos, sp] for pos, sp in zip(position, speed)]

    stack = []
    for po, sp in sorted(car)[::-1]:
        time = (target - po) / sp
        stack.append(time)
        if len(stack) >= 2 and stack[-1] <= stack[-2]:
            stack.pop()
    return len(stack)
