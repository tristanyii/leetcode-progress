# Last updated: 3/15/2026, 6:08:35 AM
1class Solution:
2    def numIslands(self, grid: List[List[str]]) -> int:
3        if not grid:
4            return 0
5
6        rows = len(grid)
7        columns = len(grid[0])
8        islands = 0
9        visited = set()
10
11        def dfs(grid, r, c):
12            if r < 0 or c < 0 or r >= rows or c >= columns:
13                return
14            if (r,c )in visited:
15                return
16            if grid[r][c] == '0':
17                return
18
19            visited.add((r,c))
20            
21            grid[r][c] = '0'
22
23            dfs(grid, r+1, c)
24            dfs(grid, r-1, c)
25            dfs(grid, r, c+1)
26            dfs(grid, r, c-1)
27
28
29        for r in range(rows):
30            for c in range(columns):
31                if grid[r][c] == '1':
32                    islands += 1
33                    dfs(grid, r, c)      
34
35        return islands  