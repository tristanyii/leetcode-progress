# Last updated: 1/12/2026, 3:13:27 PM
class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        for i in range(len(nums)-1):
            j = i+1
            if nums[i]%2==nums[j]%2:
                return False
        return True

        