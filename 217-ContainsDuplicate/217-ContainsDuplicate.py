# Last updated: 9/1/2025, 9:08:38 PM
class Solution(object):
    def containsDuplicate(self, nums):
        setmap = set()
        for num in nums:
            if num in setmap:
                return True
            setmap.add(num)
        return False

