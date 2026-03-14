# Last updated: 3/14/2026, 3:24:25 PM
1class Solution:
2    def maxProfit(self, prices: List[int]) -> int:
3        min_price = float('inf')
4        max_profit = 0
5
6        for price in prices:
7            min_price = min(min_price, price)
8            max_profit = max(max_profit, price - min_price)
9        return max_profit
10
11
12
13
14
15
16