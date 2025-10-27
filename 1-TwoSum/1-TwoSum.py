# Last updated: 10/27/2025, 12:08:16 AM
class Solution(object):
    def twoSum(self, nums, target):
        pair_idx = {}

        for i, num in enumerate(nums):
            if target - num in pair_idx:
                return [i, pair_idx[target - num]]
            pair_idx[num] = i