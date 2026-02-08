# Last updated: 2/7/2026, 11:50:09 PM
1class Solution:
2    def numRescueBoats(self, people: List[int], limit: int) -> int:
3        sw = sorted(people)
4        l, r = 0, len(people) - 1
5        boats = 0
6
7        while l <= r:
8            if sw[l] + sw[r] <= limit:
9                boats += 1
10                l += 1
11                r -= 1
12            else:
13                r -= 1
14                boats += 1
15        return boats
16            
17                
18
19        