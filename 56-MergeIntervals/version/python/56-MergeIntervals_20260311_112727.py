# Last updated: 3/11/2026, 11:27:27 AM
1class Solution:
2    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
3        intervals.sort()
4        prev = intervals[0]
5        ans = []
6
7        for interval in intervals[1::]:
8            if prev[1] >= interval[0]:
9                prev[1] = max(prev[1], interval[1])
10            else:
11                ans.append(prev)
12                prev = interval
13        ans.append(prev)
14        return ans
15
16
17
18        