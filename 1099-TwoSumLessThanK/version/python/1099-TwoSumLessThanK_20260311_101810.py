# Last updated: 3/11/2026, 10:18:10 AM
1class Solution:
2    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
3        nums.sort()
4        l, r = 0, len(nums) - 1
5        best = -1
6
7        while l < r:
8            num_sum = nums[l] + nums[r]
9            if num_sum < k: #does not acount the highest closest
10                best = max(best, num_sum)
11                l+= 1
12            else: 
13                r-= 1
14        return best
15            