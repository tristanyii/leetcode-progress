# Last updated: 3/8/2026, 12:19:51 AM
1class Solution:
2    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
3        intervals.sort()
4        prev = intervals[0]
5        output = []
6
7        for interval in intervals[1:]:
8            if interval[0] <= prev[1]:
9                prev[1] = max(prev[1], interval[1])
10            else:
11                output.append(prev)
12                prev = interval
13
14        output.append(prev)
15        return output