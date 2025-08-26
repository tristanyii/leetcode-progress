# Last updated: 8/26/2025, 12:31:55 AM
class Solution(object):
    def moveZeroes(self, nums):
        j = 0  # next position to place a non-zero
        for i in range(len(nums)):
            if nums[i] != 0:
                if i != j:
                    nums[j], nums[i] = nums[i], nums[j]
                j += 1
        