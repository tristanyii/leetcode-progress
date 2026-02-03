# Last updated: 2/3/2026, 11:10:06 AM
1class Solution(object):
2    def twoSum(self, nums, target):
3        hashmap = {}
4
5        for i, num in enumerate(nums):
6            complement = target - num
7            if complement in hashmap:
8                return hashmap[complement], i
9            hashmap[num] = i
10            
11 
12        