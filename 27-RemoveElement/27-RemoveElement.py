# Last updated: 10/15/2025, 12:40:04 PM
class Solution(object):
    def removeElement(self, nums, val):
        l = 0
        for r in range(l, len(nums)):
            if nums[r] != val:
                nums[l] = nums[r]
                l += 1
        return l

        
        