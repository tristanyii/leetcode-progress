# Last updated: 3/11/2026, 12:22:34 AM
1class Solution:
2    def longestCommonPrefix(self, strs: List[str]) -> str:
3        if strs == None or len(strs) == 0:
4            return ""
5        for i in range(len(strs[0])):
6            c = strs[0][i]
7            for j in range(1, len(strs)):
8                if i == len(strs[j]) or strs[j][i] != c:
9                    return strs[0][0:i]
10        return strs[0]