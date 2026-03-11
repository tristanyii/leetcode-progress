# Last updated: 3/11/2026, 11:11:26 AM
1class Solution:
2    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
3        '''
4        1 <---> 3
5            2-------->6
6        1 <---------->6
7        '''
8
9        if not intervals:
10            return []
11        intervals.sort()
12        first_interval = intervals[0]
13        ans = []
14
15        for interval in intervals[1::]:
16            merge = 0
17            if first_interval[1] >= interval[0]:
18                first_interval[1] = max(first_interval[1], interval[1])
19            else:
20                ans.append(first_interval)
21                first_interval = interval
22        ans.append(first_interval)
23        return ans
24            
25
26
27
28        
29
30
31