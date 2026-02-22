# Last updated: 2/22/2026, 12:42:35 PM
1from collections import defaultdict
2
3class Solution:
4    def firstUniqChar(self, s: str) -> int:
5
6        unique = defaultdict(int)
7
8        for letters in s:
9            unique[letters] += 1
10
11        for i, letters in enumerate(s):
12            if unique[letters] == 1:
13                return i
14
15        return -1