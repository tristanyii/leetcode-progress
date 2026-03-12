# Last updated: 3/11/2026, 11:39:43 PM
1class Solution(object):
2    def twoSum(self, nums, target):
3        hashMap = {}
4
5        for i, num in enumerate(nums):
6            complement = target - num
7            if complement in hashMap:
8                return [hashMap[complement], i]
9            hashMap[num] = i
10        