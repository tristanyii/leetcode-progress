# Last updated: 8/15/2025, 4:09:38 PM
class Solution(object):
    def findNumbers(self, nums):
        count = 0 

        for num in nums:
                if len(str(num)) % 2 == 0:
                    count += 1
        return count

        