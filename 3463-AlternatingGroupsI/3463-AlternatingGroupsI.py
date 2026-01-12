# Last updated: 1/12/2026, 3:13:22 PM
class Solution:
    def numberOfAlternatingGroups(self, colors: List[int]) -> int:
        count = 0
        n = len(colors)
        for i in range(n):
            if colors[(i-1)%n] != colors[i] and colors[(i+1)%n] != colors[i]:
                count+=1
        return count
            
