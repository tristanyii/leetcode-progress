# Last updated: 3/10/2026, 7:13:07 PM
1class Solution:
2    def lengthOfLongestSubstring(self, s: str) -> int:
3        l = 0
4        check = set()
5        longest = 0
6
7        for r in range(len(s)):
8            while s[r] in check:
9                check.remove(s[l])
10                l += 1
11            check.add(s[r])   
12
13            longest = max(longest, r-l+1)
14        return longest
15
16        