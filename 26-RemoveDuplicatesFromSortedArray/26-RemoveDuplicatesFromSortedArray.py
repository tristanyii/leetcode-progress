# Last updated: 8/12/2025, 9:16:30 PM
class Solution(object):
    def removeDuplicates(self, nums):
        if not nums:
            return 0
        
        left = 0
        for right in range(1, len(nums)):
            if nums[right] != nums[left]:
                left += 1
                nums[left] = nums[right]
        
        return left + 1