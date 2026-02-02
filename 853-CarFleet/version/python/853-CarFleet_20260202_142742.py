# Last updated: 2/2/2026, 2:27:42 PM
1class Solution:
2    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
3        stuff = list(zip(position, speed))
4
5        stack = []
6
7        for p, s in sorted(stuff)[::-1]:
8            time = (target - p) / s
9            if not stack or time > stack[-1]:
10                stack.append(time)
11
12        return len(stack)
13
14            
15        