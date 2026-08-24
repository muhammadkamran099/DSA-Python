def best_time_to_buy_and_sell(prices):
    max_profit = 0

    for i in range(len(prices) - 1):
        for j in range(i + 1, len(prices)):
            total_profit = prices[j] - prices[i]
            max_profit = max(max_profit, total_profit)

    return max_profit


prices = [7, 2, 1, 5, 6, 4, 8]

result = best_time_to_buy_and_sell(prices)

print(result)