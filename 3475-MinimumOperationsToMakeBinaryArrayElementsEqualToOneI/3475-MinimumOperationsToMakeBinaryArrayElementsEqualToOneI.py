# Last updated: 1/12/2026, 3:13:19 PM
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        state = {}
        count = 0
        for i in range(2, len(nums)):
            if nums[i-2] == 0:
                count+=1
                nums[i-2] = nums[i-2] ^ 1
                nums[i-1] = nums[i-1] ^ 1
                nums[i] = nums[i] ^ 1
        if sum(nums) == len(nums):
            return count
        return -1
