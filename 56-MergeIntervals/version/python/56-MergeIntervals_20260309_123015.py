# Last updated: 3/9/2026, 12:30:15 PM
1class Solution:
2    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
3#constraints/clarifying questions: are touching intervals overlapping?, is the array guranteed to be nonempty? is it already sorted?
4    #1<---->3
5     #   2<---->6
6     # if not sorted, sort the array first because we could miss potential overlaps
7        if not intervals:
8            return []
9        intervals.sort()
10        ans = []
11        prev = intervals[0]
12
13        for interval in intervals[1::]:
14            if prev[1] >= interval[0]:
15                prev[1] = max(prev[1], interval[1])
16            else:
17                ans.append(prev)
18                prev = interval
19        ans.append(prev)
20        return ans
21
22
23
24
25
26
27