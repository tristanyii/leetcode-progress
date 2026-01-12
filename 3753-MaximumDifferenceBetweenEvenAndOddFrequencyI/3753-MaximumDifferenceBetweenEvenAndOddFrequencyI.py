# Last updated: 1/12/2026, 3:12:53 PM
class Solution:
    def maxDifference(self, s: str) -> int:
        arr = [0] * 26
        for c in s:
            arr[ord(c)-ord('a')] += 1
        maxOdd = max(c for c in arr if c%2==1)
        minEven = min(c for c in arr if c%2==0 and c > 0)
        return maxOdd - minEven