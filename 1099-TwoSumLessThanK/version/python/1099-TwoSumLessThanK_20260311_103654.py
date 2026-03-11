# Last updated: 3/11/2026, 10:36:54 AM
1class Solution:
2    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
3        if not nums:
4            return -1
5
6        nums.sort()
7        ans = -1
8        l, r = 0, len(nums) - 1
9
10        while l < r:
11            total = nums[l] + nums[r]
12            
13            if total < k:
14                ans = max(total, ans)
15                l += 1
16            else: 
17                r -= 1
18
19        return ans 
20
21    