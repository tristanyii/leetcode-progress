# Last updated: 3/14/2026, 3:04:02 PM
1class Solution:
2    def lengthOfLongestSubstring(self, s: str) -> int:
3        left = 0
4        check = set()
5        max_len = 0
6
7        #s = "abcabcbb"
8        for right in range(len(s)):
9            while s[right] in check:
10                check.remove(s[left])
11                left += 1
12            check.add(s[right])
13            max_len = max(max_len, right - left + 1)
14
15        return max_len