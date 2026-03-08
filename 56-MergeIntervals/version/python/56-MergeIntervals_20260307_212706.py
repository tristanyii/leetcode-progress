# Last updated: 3/7/2026, 9:27:06 PM
1class Solution:
2    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
3        intervals.sort()
4        output = []
5        prev = intervals[0]
6        for interval in intervals:
7            if interval == prev:
8                continue
9            if interval[0]<=prev[1]:
10                prev[1] = max(interval[1], prev[1])
11            else:
12                output.append(prev)
13                prev = interval
14        output.append(prev)
15        return output
16        
17