# Last updated: 3/7/2026, 9:27:49 PM
1class Solution:
2    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
3        intervals.sort()
4        output = []
5        prev = intervals[0]
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