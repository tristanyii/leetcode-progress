# Last updated: 3/11/2026, 2:03:13 PM
1class Solution(object):
2    def twoSum(self, nums, target):
3        hashMap = {}
4
5        for i, num in enumerate(nums):
6            complement = target - num
7            if complement in hashMap:
8
9                return [hashMap[complement], i]
10            hashMap[num] = i
11
12
13        
14
15            
16 
17        