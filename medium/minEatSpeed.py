def minEatingSpeed(piles: list[int], h: int) -> int:
    if len(piles) == h:
        return max(piles)
    left = 1
    right = max(piles)

    # total_hour = len(piles)
    all_min = max(piles)

    while left <= right:
        mid = (left + right) // 2
        # print(left)
        # print(right)
        print(mid)

        current_min = findHour(piles, mid)
        print(f"current min {current_min}")

        if current_min == all_min:
            return all_min

        if current_min > h:
            left = mid + 1
        else:
            right = mid - 1
            if current_min <= h and mid < all_min:
                all_min = mid
                # right = mid - 1

    return all_min


def findHour(piles, rate):
    total = 0
    for i in piles:
        num = (i + rate - 1) // rate
        total += num
    return total


# piles = [25, 10, 23, 4]
# h = 4
# piles = [1, 4, 3, 2]
# h = 9


piles = [3, 6, 7, 11]
h = 8  # 4
print(minEatingSpeed(piles, h))
