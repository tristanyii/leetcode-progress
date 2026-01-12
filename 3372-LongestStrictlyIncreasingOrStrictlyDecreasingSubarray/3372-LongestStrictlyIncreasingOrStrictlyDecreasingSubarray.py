# Last updated: 1/12/2026, 3:13:34 PM
class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        isIncreasing = True
        highestLen = 1
        l = 0
        r = 1
        while(r<len(nums)):
            if isIncreasing and nums[r-1] < nums[r]:
                highestLen = max(highestLen,r-l+1)
            elif isIncreasing:
                isIncreasing = False
                l = r-1
            if not isIncreasing and nums[r-1] > nums[r]:
                highestLen = max(highestLen,r-l+1)
            elif not isIncreasing:
                isIncreasing = True
                l = r-1
            if nums[r-1] == nums[r]:
                l = r
            r+=1
        return highestLen
        
            