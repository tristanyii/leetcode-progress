# Last updated: 8/15/2025, 4:18:56 PM
class Solution(object):
    def sortedSquares(self, nums):
        sort = sorted(nums)
        new = []
        for num in sort:
            new.append(num*num)
        new.sort()
        return new
        