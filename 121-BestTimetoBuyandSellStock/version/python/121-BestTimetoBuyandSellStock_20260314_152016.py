# Last updated: 3/14/2026, 3:20:16 PM
1class Solution:
2    def maxProfit(self, prices: List[int]) -> int:
3        left = 0
4        most_profit = 0
5
6        for right in range(len(prices)):
7            profit = prices[right] - prices[left]
8            if prices[right] < prices[left]:
9                left = right
10            most_profit = max(most_profit, profit)
11        return most_profit
12
13
14
15
16
17
18
19