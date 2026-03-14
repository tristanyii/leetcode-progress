# Last updated: 3/14/2026, 1:42:41 AM
1class Solution:
2    def subarraySum(self, nums: List[int], k: int) -> int:
3        prefix_sums = defaultdict(int)
4        counts = 0
5        prefix_sum = 0
6        prefix_sums[0] = 1
7
8        for num in nums:
9            prefix_sum += num
10            counts += prefix_sums[prefix_sum - k]
11            prefix_sums[prefix_sum] += 1
12
13        return counts
14        