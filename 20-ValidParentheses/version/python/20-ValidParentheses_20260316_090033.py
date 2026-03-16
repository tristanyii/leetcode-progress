# Last updated: 3/16/2026, 9:00:33 AM
1class Solution:
2    def isValid(self, s: str) -> bool:
3        stack = []
4        pairs = {')':'(', ']':'[', '}':'{'}
5
6        for c in s:
7            if c in pairs:
8                if not stack or stack[-1] != pairs[c]:
9                    return False
10                stack.pop()
11            else:
12                stack.append(c)
13        return not stack