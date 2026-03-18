# Last updated: 3/18/2026, 10:19:40 AM
1class Solution:
2    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
3        i = 0
4        j = 0
5        res = []
6
7        while i < m and j < n:
8            if nums1[i] <= nums2[j]:
9                res.append(nums1[i])
10                i+= 1
11
12            else:
13                res.append(nums2[j])
14                j+= 1
15
16        while i < m:
17            res.append(nums1[i])
18            i += 1
19        while j < n:
20            res.append(nums2[j])
21            j += 1
22        nums1[:] = res
23
24
25
26        
27       
28