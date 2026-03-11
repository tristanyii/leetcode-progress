# Last updated: 3/10/2026, 11:34:58 PM
1class Solution:
2    def maxProfit(self, prices: List[int]) -> int:
3        minprices = prices[0]
4        maxprice = 0
5
6        for price in prices:
7            minprices = min(minprices, price)
8            maxprice = max(maxprice, price - minprices)
9
10        return maxprice
11
12
13
14
15
16