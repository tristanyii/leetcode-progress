# Last updated: 1/12/2026, 3:12:39 PM
class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        n = len(grid)
        m = len(grid[0])

        #instantiate prefix sum grids
        horz_prefix_grid = [0 for i in range(n)]
        vert_prefix_grid = [0 for j in range(m)]

        #populate horizontal prefix sum grid
        for i in range(n):
            if i == 0:
                horz_prefix_grid[0] = sum(grid[0])
            else:
                horz_prefix_grid[i] = horz_prefix_grid[i-1] + sum(grid[i])
            
        #populate vertical prefix sum grid
        for j in range(m):
            col_sum = 0
            for i in range(n):
                col_sum += grid[i][j]
            if j == 0:
                vert_prefix_grid[0] = col_sum
            else:
                vert_prefix_grid[j] = vert_prefix_grid[j-1] + col_sum

        #iterate through all possible horz cuts
        for cut in range(1,n):
            if horz_prefix_grid[cut-1] == horz_prefix_grid[n-1] - horz_prefix_grid[cut-1]:
                return True

        #iterate through all possible vertical cuts
        for cut in range(1,m):
            if vert_prefix_grid[cut-1] == vert_prefix_grid[m-1] - vert_prefix_grid[cut-1]:
                return True

        #if couldn't find valid cut, quit False
        return False
        
