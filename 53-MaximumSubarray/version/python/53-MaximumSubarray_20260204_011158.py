# Last updated: 2/4/2026, 1:11:58 AM
1class Solution:
2    def maxSubArray(self, nums: List[int]) -> int:
3        maxSub = nums[0]
4        currSub = 0
5
6        for num in nums:
7            if currSub < 0:
8                currSub = 0
9            currSub += num
10
11            maxSub = max(maxSub, currSub)
12        return maxSub
13