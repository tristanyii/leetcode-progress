# Last updated: 3/14/2026, 1:47:36 AM
1class Solution:
2    def singleNumber(self, nums: List[int]) -> int:
3        countMap = defaultdict(int)
4
5        for num in nums:
6            countMap[num] += 1
7        for num in countMap:
8            if countMap[num] == 1:
9                return num
10        