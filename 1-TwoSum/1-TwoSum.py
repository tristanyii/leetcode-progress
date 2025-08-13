# Last updated: 8/12/2025, 9:16:15 PM
class Solution(object):
    def twoSum(self, nums, target):
        for num1 in range(len(nums)):
            for num2 in range(num1 + 1, len(nums)):
                if nums[num1] + nums[num2] == target:
                    return [num1, num2]
