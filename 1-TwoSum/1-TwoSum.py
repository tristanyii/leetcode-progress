# Last updated: 8/22/2025, 7:57:43 PM
class Solution(object):
    def twoSum(self, nums, target):
        for num1 in range(len(nums)):
            for num2 in range(num1 + 1, len(nums)):
                if nums[num1] + nums[num2] == target:
                    return [num1, num2]
