# Last updated: 3/11/2026, 12:11:13 PM
1from collections import defaultdict
2class Solution:
3    def isAnagram(self, s: str, t: str) -> bool:
4        valid_anagram = defaultdict(int)
5
6        if len(s) != len(t):
7            return False
8
9        for char in s:
10            valid_anagram[char] += 1
11
12        for char in t:
13            valid_anagram[char] -= 1
14
15        for values in valid_anagram.values():
16            if values != 0:
17                return False
18        return True
19        