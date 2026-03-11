# Last updated: 3/10/2026, 11:27:56 PM
1class Solution:
2    def maxProfit(self, prices: List[int]) -> int:
3        minprices = prices[0]
4        maxprofit = 0
5
6        for price in prices:
7            minprices = min(minprices, price)
8            maxprofit = max(maxprofit, price - minprices)
9            
10
11        return maxprofit
12
13
14
15
16
17
18