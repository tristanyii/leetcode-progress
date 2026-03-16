# Last updated: 3/16/2026, 7:34:02 AM
1class Solution:
2    def longestConsecutive(self, nums: List[int]) -> int:
3        num_set = set(nums)
4        longest = 0
5
6        for num in num_set:
7            if num - 1 not in num_set:
8                length = 1
9                while num + length in num_set:
10                    length += 1
11                longest = max(longest, length)
12        return longest
13
14