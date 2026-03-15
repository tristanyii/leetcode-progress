# Last updated: 3/15/2026, 6:19:36 AM
1class Solution:
2    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
3        if not grid:
4            return 0
5
6        rows = len(grid)
7        columns = len(grid[0])
8        max_area = 0
9
10        def dfs(grid, r, c):
11            if r < 0 or c < 0 or r >= rows or c >= columns:
12                return 0
13            if grid[r][c] == 0:
14                return 0
15            
16            grid[r][c] = 0
17            
18            return (1 + dfs(grid, r+1, c) + dfs(grid, r-1, c) + dfs(grid, r, c+1) + dfs(grid, r, c-1))
19
20            
21
22        for r in range(rows):
23            for c in range(columns):
24                if grid[r][c] == 1:
25                    max_area = max(max_area, dfs(grid, r, c))
26        return max_area
27