# Last updated: 3/14/2026, 2:54:59 PM
1class Solution:
2    def lengthOfLongestSubstring(self, s: str) -> int:
3        left = 0
4        check = set()
5        max_len = 0
6
7        for right in range(len(s)):
8            while s[right] in check:
9                check.remove(s[left])
10                left += 1
11            check.add(s[right])
12
13            max_len = max(max_len, right - left + 1)
14        return max_len
15            
16
17        