# Last updated: 3/5/2026, 12:58:03 PM
1import queue
2class Solution:
3    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
4        queue = deque()
5        rows, cols = len(mat), len(mat[0])
6        for row in range(rows):
7            for col in range(cols):
8                if mat[row][col] == 0:
9                    queue.append((row, col))
10                else:
11                    mat[row][col] = float('inf')
12
13        while queue:
14            r, c = queue.popleft()
15            check = [(r+1, c), (r-1, c), (r,c-1), (r,c+1)]
16            for row, col in check:
17                if 0 <= row < rows and 0 <= col < cols and mat[row][col] > mat[r][c] + 1:
18                    mat[row][col] = mat[r][c] + 1
19                    queue.append((row, col))
20        return mat
21        