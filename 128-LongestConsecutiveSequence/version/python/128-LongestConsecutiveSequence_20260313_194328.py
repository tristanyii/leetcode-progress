# Last updated: 3/13/2026, 7:43:28 PM
1class Solution:
2    def longestConsecutive(self, nums: List[int]) -> int:
3        nums = set(nums)
4        best = 0
5
6        for num in nums:
7            if num - 1 not in nums:
8                num1 = num + 1
9                while num1 in nums:
10                    num1 += 1
11                best = max(best, num1 - num)
12        return best