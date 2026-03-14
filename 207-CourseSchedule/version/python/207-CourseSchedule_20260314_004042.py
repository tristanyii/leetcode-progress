# Last updated: 3/14/2026, 12:40:42 AM
1from collections import defaultdict
2
3class Solution:
4    def canFinish(self, numCourses, prerequisites):
5
6        graph = defaultdict(list)
7
8        for course, pre in prerequisites:
9            graph[course].append(pre)
10
11        state = [0] * numCourses
12
13        def dfs(course):
14
15            if state[course] == 1:
16                return False
17
18            if state[course] == 2:
19                return True
20
21            state[course] = 1
22
23            for pre in graph[course]:
24                if not dfs(pre):
25                    return False
26
27            state[course] = 2
28            return True
29
30        for course in range(numCourses):
31            if not dfs(course):
32                return False
33
34        return True