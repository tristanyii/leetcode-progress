# Last updated: 3/10/2026, 1:37:27 PM
1class Solution:
2    def numIslands(self, grid: List[List[str]]) -> int:
3        if not grid:
4            return 0
5
6        islands = 0
7        for r in range(len(grid)):
8            for c in range(len(grid[r])):
9                if grid[r][c] == '1':
10                    self.dfs(grid, r, c)
11                    islands += 1
12        return islands
13    
14    def dfs(self, grid, r, c):
15        grid[r][c] = '0'
16        lst = [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]
17        for row, column in lst:
18            if row >=0 and column >= 0 and row < len(grid) and column < len(grid[row]) and grid[row][column] == '1':
19                self.dfs(grid, row, column)
20
21        
22
23        
24
25
26        
27
28
29        