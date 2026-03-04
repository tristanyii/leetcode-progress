# Last updated: 3/3/2026, 7:36:42 PM
1class Solution:
2    def threeSum(self, nums: list[int]) -> list[list[int]]:
3        #sort so [-1,0,1,2,-1,-4] turns to [-4, -1, -1, 0, 1, 2]
4
5        #two pointer to find every posible combination that a + b + c = 0
6        nums.sort()
7        ans = []
8
9        for i, num in enumerate(nums):
10            l, r = i + 1, len(nums) - 1
11            if i > 0 and nums[i] == nums[i - 1]:
12                continue
13
14            while l < r:
15                if l > i + 1 and nums[l] == nums[l - 1]:
16                    l += 1
17                    continue
18                if r < len(nums) - 1 and nums[r] == nums[r + 1]:
19                    r -= 1
20                    continue
21
22                if nums[i] + nums[l] + nums[r] == 0:
23                    ans.append([nums[i], nums[l], nums[r]])
24                    l += 1
25                elif nums[i] + nums[l] + nums[r] < 0:
26                    l += 1
27                elif nums[i] + nums[l] + nums[r] > 0:
28                    r -= 1
29        
30        return ans
31
32                
33
34
35
36
37        