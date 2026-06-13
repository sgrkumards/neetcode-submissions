class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price  = prices[0]
        max_profit = 0
        for price in range(1, len(prices)):
            min_price = min(min_price, prices[price])
            profit = prices[price] - min_price
            max_profit = max(profit, max_profit)
        return max_profit
