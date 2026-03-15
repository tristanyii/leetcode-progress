# Last updated: 3/15/2026, 3:55:27 PM
1class Solution:
2    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
3        intervals.sort()
4        first_interval = intervals[0]
5        res = []
6
7        for interval in intervals[1::]:
8            if first_interval[1] >= interval[0]:
9                first_interval[1] = max(first_interval[1], interval[1])
10            else:
11                res.append(first_interval)
12                first_interval = interval
13        res.append(first_interval)
14        return res  
15
16        
17                