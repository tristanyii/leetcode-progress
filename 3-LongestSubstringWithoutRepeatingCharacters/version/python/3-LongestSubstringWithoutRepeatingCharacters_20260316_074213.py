# Last updated: 3/16/2026, 7:42:13 AM
1class Solution:
2    def lengthOfLongestSubstring(self, s: str) -> int:
3        check = set()
4        l = 0
5        longest = 0
6
7        for r in range(len(s)):
8            while s[r] in check:
9                check.remove(s[l])
10                l += 1
11
12            else:
13                check.add(s[r])
14            longest = max(longest, r - l + 1)
15        return longest
16        