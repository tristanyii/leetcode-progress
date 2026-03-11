# Last updated: 3/11/2026, 12:21:10 AM
1class Solution:
2    def lengthOfLongestSubstring(self, s: str) -> int:
3        l = 0
4        checkSet = set()
5        longest = 0
6        for r in range(len(s)):
7            while s[r] in checkSet:
8                checkSet.remove(s[l])
9                l += 1
10            else:
11                checkSet.add(s[r])
12                longest = max(longest, r - l + 1)
13        return longest
14
15