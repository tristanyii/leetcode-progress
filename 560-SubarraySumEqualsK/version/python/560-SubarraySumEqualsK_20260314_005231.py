# Last updated: 3/14/2026, 12:52:31 AM
1class Solution:
2    def subarraySum(self, nums, k):
3        count = 0
4        prefix = 0
5        seen = {0:1}
6
7        for num in nums:
8            prefix += num
9
10            if prefix - k in seen:
11                count += seen[prefix - k]
12
13            if prefix in seen:
14                seen[prefix] += 1
15            else:
16                seen[prefix] = 1
17
18        return count