# Last updated: 2/9/2026, 2:27:50 PM
1class Solution:
2    def reverseString(self, s: List[str]) -> None:
3        l, r = 0, len(s) - 1
4
5        while l <= r:
6            s[l], s[r] = s[r], s[l]
7            l += 1
8            r -= 1
9        return s
10        