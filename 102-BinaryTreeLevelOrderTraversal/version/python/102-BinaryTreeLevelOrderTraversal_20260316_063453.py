# Last updated: 3/16/2026, 6:34:53 AM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
9        if not root:
10            return []
11        q = deque([root])
12        result = []
13
14        while q:
15            level = []
16
17            for _ in range(len(q)):
18                node = q.popleft()
19                level.append(node.val)
20                if node.left:
21                    q.append(node.left)
22                if node.right:
23                    q.append(node.right)
24            result.append(level)
25        return result
26
27        