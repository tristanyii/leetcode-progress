# Last updated: 3/14/2026, 3:27:02 PM
1class Solution:
2    def numIslands(self, grid: List[List[str]]) -> int:
3        if not grid:
4            return 0
5
6        rows = len(grid)
7        cols = len(grid[0])
8        islands = 0
9
10        for r in range(rows):
11            for c in range(cols):
12                if grid[r][c] == "1":
13                    islands += 1
14                    self.dfs(grid, r, c)
15
16        return islands
17
18
19    def dfs(self, grid, r, c):
20        if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]) or grid[r][c] == "0":
21            return
22
23        grid[r][c] = "0"
24
25        self.dfs(grid, r+1, c)
26        self.dfs(grid, r-1, c)
27        self.dfs(grid, r, c+1)
28        self.dfs(grid, r, c-1)