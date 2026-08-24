def best_time_to_buy_and_sell(prices):
    max_profit = 0
    min_price = float("inf")

    for price in prices:
        min_price = min(min_price, price)
        max_profit = max(max_profit, price - min_price)

    return max_profit


prices = [7, 2, 1, 5, 6, 4, 8, 3]

result = best_time_to_buy_and_sell(prices)

print(result)