# Last updated: 9/7/2025, 5:37:28 PM
class Solution(object):
    def maxProfit(self, prices):
        l, r = 0, 1
        maxP = 0

        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxP = max(maxP, profit)
            else:
                l = r
            r += 1
        return maxP

        


        