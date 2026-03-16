# Last updated: 3/16/2026, 6:03:34 AM
1from collections import deque
2
3class Solution:
4    def orangesRotting(self, grid: List[List[int]]) -> int:
5        if not grid:
6            return 0
7        
8        q = deque()
9        rows = len(grid)
10        columns = len(grid[0])
11        fresh = 0
12
13        for r in range(rows):
14            for c in range (columns):
15                if grid[r][c] == 1:
16                    fresh += 1
17                if grid[r][c] == 2:
18                    q.append((r, c))
19        
20        minutes = 0
21        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
22        
23        while q and fresh > 0:
24            for _ in range(len(q)):
25                r, c = q.popleft()
26                for dr, dc in directions:
27                    nr = r + dr
28                    nc = c + dc
29
30                    if 0 <= nr < rows and 0 <= nc < columns and grid[nr][nc] == 1:
31                        grid[nr][nc] = 2
32                        fresh -= 1
33                        q.append((nr, nc))
34            minutes += 1
35        
36        return minutes if fresh == 0 else -1
37
38