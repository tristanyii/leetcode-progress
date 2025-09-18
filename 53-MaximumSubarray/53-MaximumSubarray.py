# Last updated: 9/18/2025, 12:58:46 AM
class Solution(object):
    def maxSubArray(self, nums):
        maxSub = nums[0]
        currSub = 0

        for n in nums:
            if currSub < 0:
                currSub = 0
            currSub += n
            maxSub = max(currSub, maxSub)
        return maxSub
            
        