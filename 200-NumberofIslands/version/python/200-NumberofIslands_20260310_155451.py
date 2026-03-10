# Last updated: 3/10/2026, 3:54:51 PM
1class Solution:
2    def numIslands(self, grid: List[List[str]]) -> int:
3        if not grid:
4            return 0
5
6
7        islands = 0 
8        for r in range(len(grid)):
9            for c in range(len(grid[r])):
10                if grid[r][c] == '1':
11                    self.dfs(grid, r, c)
12                    islands += 1
13        return islands
14
15    def dfs(self, grid, r, c):
16        grid[r][c] = '0'
17        directions = [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]
18        for row, column in directions:
19            if row >= 0 and column >= 0 and row < len(grid) and column < len(grid[row]) and grid[row][column] == '1':
20                self.dfs(grid, row, column)
21
22