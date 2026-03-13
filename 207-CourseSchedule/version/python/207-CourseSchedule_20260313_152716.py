# Last updated: 3/13/2026, 3:27:16 PM
1from collections import defaultdict
2
3class Solution:
4    def canFinish(self, numCourses, prerequisites):
5        graph = defaultdict(list)
6
7        for a, b in prerequisites:
8            graph[a].append(b)
9
10        state = [0] * numCourses   # 0=unvisited,1=visiting,2=done
11
12        def dfs(course):
13            if state[course] == 1:
14                return False   # cycle found
15            
16            if state[course] == 2:
17                return True
18
19            state[course] = 1
20
21            for pre in graph[course]:
22                if not dfs(pre):
23                    return False
24
25            state[course] = 2
26            return True
27
28        for c in range(numCourses):
29            if not dfs(c):
30                return False
31
32        return True
33