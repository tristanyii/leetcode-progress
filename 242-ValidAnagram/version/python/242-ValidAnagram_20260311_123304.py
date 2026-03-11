# Last updated: 3/11/2026, 12:33:04 PM
1class Solution:
2    def isAnagram(self, s: str, t: str) -> bool:
3        if len(s) != len(t):
4            return False
5
6        count = [0] * 26
7
8        for i in range(len(s)):
9            count[ord(s[i]) - ord('a')] += 1
10            count[ord(t[i]) - ord('a')] -= 1
11
12        # Explicit check (like your dictionary version)
13        for value in count:
14            if value != 0:
15                return False
16
17        return True