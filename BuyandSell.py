def buy_and_sell(prices):
    if not prices:
        return 0

    min_price = prices[0]
    max_profit=0
    for price in prices:
        min_price = min(min_price,price)
        max_profit = max(max_profit, price - min_price)
    return max_profit
input_prices = list(map(int,input("Enter the prices separated by space:").split()))
result = buy_and_sell(input_prices)
if result > 0:
    print("The maximum profit that can be achieved is:",result)
else:
    print("No profit can be achieved from the given prices.")

#which day to buy and sell the stock to maximize profit
def buy_and_sell_days(prices):
    if not prices:
        return None, None

    min_price = prices[0]
    max_profit = 0
    buy_day = 0
    sell_day = 0

    for i in range(len(prices)):
        if prices[i] < min_price:
            min_price = prices[i]
            buy_day = i
        elif prices[i] - min_price > max_profit:
            max_profit = prices[i] - min_price
            sell_day = i

    if max_profit > 0:
        return buy_day, sell_day
    else:
        return None, None
prices = list(map(int, input("Enter the prices separated by space: ").split()))
buy_day, sell_day = buy_and_sell_days(prices)
if buy_day is not None and sell_day is not None:
    print(f"Buy on day {buy_day} and sell on day {sell_day} to maximize profit.")
