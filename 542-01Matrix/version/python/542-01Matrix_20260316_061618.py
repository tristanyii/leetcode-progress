# Last updated: 3/16/2026, 6:16:18 AM
1class Solution:
2    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
3        q = deque()
4        rows = len(mat)
5        columns = len(mat[0])
6
7        for r in range(rows):
8            for c in range(columns):
9                if mat[r][c] == 0:
10                    q.append((r, c))
11                else:
12                    mat[r][c] = float('inf')
13
14        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
15
16        while q:
17            for _ in range(len(q)):
18                r, c = q.popleft()
19
20                for dr, dc in directions:
21                    nr = r + dr
22                    nc = c + dc
23                    
24                    if 0 <= nr < rows and 0 <= nc < columns:
25                        if mat[nr][nc] > mat[r][c]:
26                            mat[nr][nc] = mat[r][c] + 1
27                            q.append((nr, nc)) 
28
29        return mat
30        
31