# Last updated: 12/31/2025, 4:35:08 PM
1class Solution(object):
2    def twoSum(self, nums, target):
3        seen = {}
4
5        for i, curr in enumerate(nums):
6            complement = target - curr
7
8            if complement in seen:
9                return [seen[complement], i]
10
11            seen[curr] = i
12
13
14        
15        ''' so firstly, i set complement as what im trying to find in my hashmap.
16            i iterate through my array nums and if i find it, i return the indexes 
17            of it
18
19'''
20
21        
22