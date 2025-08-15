# Last updated: 8/15/2025, 3:56:20 PM
class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        count = 0
        current = 0
        
        for num in nums:
            if num == 1:
                current += 1
            else:
                current = 0
            count = max(current, count)
        
        return count
        