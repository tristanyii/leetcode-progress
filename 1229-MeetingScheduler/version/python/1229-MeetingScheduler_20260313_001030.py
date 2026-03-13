# Last updated: 3/13/2026, 12:10:30 AM
1class Solution:
2    def minAvailableDuration(self, slot1: List[List[int]], slot2: List[List[int]], duration: int) -> List[int]:
3
4        slot1.sort()
5        slot2.sort()
6
7        i = 0
8        j = 0
9        while i < len(slot1) and j < len(slot2):
10            start = max(slot1[i][0], slot2[j][0])
11            end = min(slot1[i][1], slot2[j][1])
12
13            if end - start >= duration:
14                return [start, start + duration]
15
16            if slot1[i][1] < slot2[j][1]:
17                i += 1
18            else:
19                j += 1
20        return []
21
22
23        