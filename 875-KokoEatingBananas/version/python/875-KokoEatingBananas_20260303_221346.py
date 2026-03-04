# Last updated: 3/3/2026, 10:13:46 PM
1import math
2class Solution:
3    def minEatingSpeed(self, piles: List[int], h: int) -> int:
4        max_pile = max(piles)
5        l, r = 1, max_pile
6        while l != r:
7            hours = 0
8            mid = ((l + r) // 2)
9            for pile in piles:
10                hours += math.ceil(pile / mid)
11            if hours <= h:
12                r = mid
13            if hours > h:
14                l = mid + 1
15        return l
16 #[3, 6, 7, 11] h = 8
17            
18                
19
20
21
22
23
24
25
26
27            
28
29
30
31                
32
33        
34