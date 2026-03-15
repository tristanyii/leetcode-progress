# Last updated: 3/15/2026, 3:22:52 PM
1from collections import deque
2
3class Solution:
4    def orangesRotting(self, grid: List[List[int]]) -> int:
5        q = deque()
6        fresh, time = 0, 0
7
8        rows = len(grid)
9        columns = len(grid[0])
10
11        for r in range(rows):
12            for c in range(columns):
13                if grid[r][c] == 1:
14                    fresh += 1
15                if grid[r][c] == 2:
16                    q.append([r, c])
17
18        directions = [(1,0), (-1,0), (0,1), (0,-1)]
19
20        while q and fresh > 0:
21            for _ in range(len(q)):
22                r, c = q.popleft()
23                for dr, dc in directions:
24                    row, col = r + dr, c + dc
25
26                    if (row < 0 or row >= rows or
27                        col < 0 or col >= columns or
28                        grid[row][col] != 1):
29                        continue
30
31                    grid[row][col] = 2
32                    fresh -= 1
33                    q.append([row, col])
34
35            time += 1
36
37        return time if fresh == 0 else -1