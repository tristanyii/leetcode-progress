# Last updated: 3/15/2026, 5:43:43 PM
1class Solution(object):
2    def twoSum(self, nums, target):
3        if not nums:
4            return []
5
6        hash_map = {}
7
8        for i, num in enumerate(nums):
9            complement = target - num
10            if complement in hash_map:
11                return [hash_map[complement], i]
12            hash_map[num] = i
13            