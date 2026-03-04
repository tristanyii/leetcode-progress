# Last updated: 3/3/2026, 10:41:31 PM
1class Solution:
2    def lengthOfLongestSubstring(self, s: str) -> int:
3        if not s:
4            return 0
5
6        dupe = set()
7        l, r = 0, 0
8        ans = 0
9
10        while r < len(s):
11            while s[r] in dupe:
12                dupe.remove(s[l])
13                l += 1
14            dupe.add(s[r])
15            ans = max(r - l + 1, ans)
16            r += 1
17        return ans
18
19
20
21
22
23
24
25
26        
27        