# Last updated: 2/5/2026, 11:39:29 PM
1class Solution:
2    def maxProfit(self, prices: List[int]) -> int:
3        min_price = prices[0]
4        max_price = 0
5
6        for price in prices:
7            min_price = min(min_price, price)
8            max_price = max(max_price, price - min_price)
9        
10        return max_price
11
12
13
14
15
16
17
18