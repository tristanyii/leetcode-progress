# Last updated: 3/15/2026, 8:01:35 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
9        q = deque([root])
10        res = []
11
12        while q:
13            qLen = len(q)
14            level = []
15            for i in range(qLen):
16                node = q.popleft()
17                if node:
18                    level.append(node.val)
19                    q.append(node.left)
20                    q.append(node.right)
21            if level: 
22                res.append(level)
23        return res
24            
25
26
27        