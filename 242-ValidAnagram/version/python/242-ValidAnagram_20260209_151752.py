# Last updated: 2/9/2026, 3:17:52 PM
1from collections import defaultdict
2
3class Solution:
4    def isAnagram(self, s: str, t: str) -> bool:
5        counter = defaultdict(int)
6
7        if len(s) != len(t):
8            return False
9
10        for char in s:
11            counter[char] += 1
12
13        for char in t:
14            counter[char] -= 1
15
16        for v in counter.values():
17            if v != 0:
18                return False
19        return True
20        