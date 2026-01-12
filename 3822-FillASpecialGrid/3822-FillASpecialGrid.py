# Last updated: 1/12/2026, 3:12:46 PM
class Solution:
    def __init__(self):
        self.grid = []

    def fillGrid(self, x, y, size, offset):
        if size == 1:
            self.grid[x][y] = offset
            return

        half = size // 2
        blockSize = half * half

        self.fillGrid(x, y, half, offset + 3 * blockSize)          # Q0
        self.fillGrid(x, y + half, half, offset)                    # Q1
        self.fillGrid(x + half, y + half, half, offset + blockSize) # Q2
        self.fillGrid(x + half, y, half, offset + 2 * blockSize)   # Q3

    def specialGrid(self, N: int) -> List[List[int]]:
        size = 1 << N  # 2^N
        self.grid = [[0] * size for _ in range(size)]  # Initialize the grid with 0s
        self.fillGrid(0, 0, size, 0)
        return self.grid
        #square grid of side length: 2^n
        #fill grid to make it "special"


    #special:
    # 1. #'s in top right quarter < #'s in bottom right quarter
    # 2. #'s in bottom right quarter < #'s in bottom left quarter
    # 3. #'s in bottom left quarter < #'s in top left quarter
    # 4. #Each quarter must also be special
        #have to view subgrids

    #0, 0, 0, 0, 15, 8, 3, 0
    #0, 0, 0, 0, 14, 13, 2, 1
    #0, 0, 0, 0, 11, 8, 7, 4
    #0, 0, 0, 0, 10, 9, 6, 5
    #0, 0, 0, 0, 31, 28, 19, 16
    #0, 0, 0, 0, 30, 29, 18, 17
    #0, 0, 0, 0, 27, 24, 23, 20
    #0, 0, 0, 0, 26, 25, 22, 21