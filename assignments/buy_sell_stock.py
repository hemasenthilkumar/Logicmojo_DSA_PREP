def maxProfit(prices) -> int:
        buy = 0
        sell = 1
        profit = 0
        while sell < len(prices):
            if prices[sell] <= prices[buy]:
                buy = sell
            else:
                profit = max(profit, prices[sell]-prices[buy])
            sell += 1
        return profit