# Last updated: 3/14/2026, 11:35:17 PM
1class Solution:
2    def numIslands(self, grid: List[List[str]]) -> int:
3        if not grid:
4            return 0
5
6
7        def dfs(r, c):
8            if r < 0 or c < 0 or r >= row or c >= column:
9                return
10            if grid[r][c] == '0':
11                return
12            grid[r][c] = '0'
13
14            dfs(r+1, c)
15            dfs(r-1, c)
16            dfs(r, c+1)
17            dfs(r, c-1)
18        
19        
20        row = len(grid)
21        column = len(grid[0])
22        islands = 0
23
24        for r in range(row):
25            for c in range(column):
26                if grid[r][c] == '1':
27                    islands += 1
28                    dfs(r, c)
29        return islands
30