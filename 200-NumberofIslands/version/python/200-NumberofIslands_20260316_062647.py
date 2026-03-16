# Last updated: 3/16/2026, 6:26:47 AM
1class Solution:
2    def numIslands(self, grid: List[List[str]]) -> int:
3        if not grid:
4            return 0
5
6        rows = len(grid)
7        columns = len(grid[0])
8        islands = 0
9
10        def dfs(grid, r, c):
11            if r < 0 or c < 0 or r >= rows or c >= columns:
12                return
13            if grid[r][c] == '0':
14                return
15
16            grid[r][c] = '0'
17
18            dfs(grid, r+1, c)
19            dfs( grid, r-1, c)
20            dfs( grid, r, c+1 )
21            dfs(grid, r, c-1)
22
23
24        for r in range(rows):
25            for c in range(columns):
26                if grid[r][c] == '1':
27                    dfs(grid, r, c)
28                    islands += 1
29
30        return islands