# Last updated: 1/12/2026, 3:13:23 PM
class Solution(object):
    def minimumArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        ROW, COL = len(grid), len(grid[0])

        left_border, right_border = float('inf'), float('-inf')
        top_border, bottom_border = float('inf'), float('-inf')
        for i in range(ROW):
            for j in range(COL):
                if grid[i][j] == 1:
                    if i < top_border:
                        top_border = i 
                    if j < left_border:
                        left_border = j 
                    break
        for x in range(ROW-1, -1, -1):
            for y in range(COL-1, -1, -1):
                if grid[x][y] == 1:
                    if y > right_border:
                        right_border = y 
                    if x > bottom_border:
                        bottom_border = x 
                    break

        print(left_border, top_border, right_border, bottom_border)
        return (bottom_border - top_border + 1) * (right_border - left_border + 1)
        