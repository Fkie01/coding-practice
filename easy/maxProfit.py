def maxProfit(prices: list[int]) -> int:
    cum_min = prices[0]
    maxProfit = 0
    for i in range(len(prices) - 1):
        # print(cum_min)
        if prices[i] > prices[i + 1]:
            continue
        else:
            if prices[i] < cum_min:
                cum_min = prices[i]
            currentProfit = prices[i + 1] - cum_min
            if currentProfit > maxProfit:
                maxProfit = currentProfit
    return maxProfit


prices = [10, 1, 5, 6, 7, 1]
print(maxProfit(prices))
prices = [10, 8, 7, 5, 2]
print(maxProfit(prices))
