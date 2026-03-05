# Last updated: 3/5/2026, 11:29:17 AM
1from typing import List
2from collections import defaultdict
3
4class Solution:
5    def subarraySum(self, nums: List[int], k: int) -> int:
6        freq = defaultdict(int)
7        freq[0] = 1  # empty prefix sum
8
9        prefix = 0
10        count = 0
11
12        for x in nums:
13            prefix += x
14            count += freq[prefix - k]
15            freq[prefix] += 1
16
17        return count