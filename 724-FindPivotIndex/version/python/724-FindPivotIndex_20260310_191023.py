# Last updated: 3/10/2026, 7:10:23 PM
1class Solution:
2    def pivotIndex(self, nums: List[int]) -> int:
3        total = sum(nums)
4
5        leftSum = 0 
6        for i in range(len(nums)):
7            rightSum = total - nums[i] - leftSum
8            if leftSum == rightSum:
9                return i
10            leftSum += nums[i]
11        return -1