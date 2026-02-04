# Last updated: 2/3/2026, 10:16:11 PM
1class Solution:
2    def lengthOfLongestSubstring(self, s: str) -> int:
3        res = 0
4        n = len(s)
5
6        freq_map = defaultdict(int)
7
8        left=0
9        for right in range(n):
10            freq_map[s[right]] += 1
11
12            while freq_map[s[right]] > 1:
13                freq_map[s[left]] -= 1
14                left += 1
15            
16            res = max(res, right - left + 1)
17        
18        return res
19
20
21from collections import Counter
22
23
24class Solution:
25    def lengthOfLongestSubstring(self, s: str) -> int:
26        chars = Counter()
27
28        left = right = 0
29
30        res = 0
31        while right < len(s):
32            r = s[right]
33            chars[r] += 1
34
35            while chars[r] > 1:
36                l = s[left]
37                chars[l] -= 1
38                left += 1
39
40            res = max(res, right - left + 1)
41
42            right += 1
43        return res
44
45class Solution:
46    def lengthOfLongestSubstring(self, s: str) -> int:
47        n = len(s)
48        ans = 0
49        # charToNextIndex stores the index after current character
50        charToNextIndex = {}
51
52        i = 0
53        # try to extend the range [i, j]
54        for j in range(n):
55            if s[j] in charToNextIndex:
56                i = max(charToNextIndex[s[j]], i)
57
58            ans = max(ans, j - i + 1)
59            charToNextIndex[s[j]] = j + 1
60
61        return ans