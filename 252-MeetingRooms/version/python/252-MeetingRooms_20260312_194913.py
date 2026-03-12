# Last updated: 3/12/2026, 7:49:13 PM
1class Solution:
2    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
3        if not intervals:
4            return True
5        intervals.sort()
6        prev = intervals[0]
7
8        for interval in intervals[1::]:
9            if prev[1] > interval[0]:
10                return False
11            prev = interval
12        return True
13
14
15        