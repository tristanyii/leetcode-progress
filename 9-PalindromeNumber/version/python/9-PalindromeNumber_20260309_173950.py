# Last updated: 3/9/2026, 5:39:50 PM
1class Solution:
2    def isPalindrome(self, x: int) -> bool:
3        if x < 0:
4            return False
5        s = str(x)
6        l, r = 0, len(s) - 1
7
8        while l < r:
9            if s[l] != s[r]:
10                return False
11            l += 1
12            r -= 1
13        return True
14
15
16