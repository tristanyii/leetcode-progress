# Last updated: 2/4/2026, 1:06:15 PM
1class Solution:
2    def maxSubArray(self, nums: List[int]) -> int:
3        maxSub = nums[0]
4        curr = 0
5
6        for num in nums:
7            if curr < 0:
8                curr = 0
9            curr += num
10            maxSub = max(maxSub, curr)
11            
12        return maxSub