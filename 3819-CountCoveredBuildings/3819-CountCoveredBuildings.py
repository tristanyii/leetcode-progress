# Last updated: 1/12/2026, 3:12:47 PM
class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        xMin, xMax = [float('inf')]*(n+1), [-float('inf')]*(n+1)
        yMin, yMax = [float('inf')]*(n+1), [-float('inf')]*(n+1)

        for x, y in buildings:
            xMin[y] = min(x, xMin[y])
            yMin[x] = min(y, yMin[x])
            xMax[y] = max(x, xMax[y])
            yMax[x] = max(y, yMax[x])

        ret = 0
        for x, y in buildings:
            if xMin[y] < x < xMax[y] and yMin[x] < y < yMax[x]:
                ret += 1
        
        return ret