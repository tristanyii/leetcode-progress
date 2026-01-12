# Last updated: 1/12/2026, 3:12:45 PM
class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        x_z = abs(x - z)
        y_z = abs(y - z)

        if x_z < y_z:
            return 1
        elif y_z < x_z:
            return 2
        return 0