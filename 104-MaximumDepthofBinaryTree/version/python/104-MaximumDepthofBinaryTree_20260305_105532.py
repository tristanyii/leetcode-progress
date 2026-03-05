# Last updated: 3/5/2026, 10:55:32 AM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7from collections import deque
8class Solution:
9    def maxDepth(self, root: Optional[TreeNode]) -> int:
10        if not root:
11            return 0
12
13        queue = deque([root])
14        depth = 0
15
16        while queue: 
17            for _ in range(len(queue)):
18                node = queue.popleft()
19
20                if node.left:
21                    queue.append(node.left)
22                if node.right:
23                    queue.append(node.right)
24
25            depth += 1
26
27        return depth
28
29        
30        