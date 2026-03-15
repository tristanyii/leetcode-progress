# Last updated: 3/14/2026, 9:36:58 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, x):
4#         self.val = x
5#         self.left = None
6#         self.right = None
7
8class Solution:
9    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
10        if not root:
11            return None
12
13        def dfs(root):
14            if not root:
15                return None
16            
17            if root == p or root == q:
18                return root
19
20            left = dfs(root.left)
21            right = dfs(root.right)
22
23            if left and right:
24                return root
25            return left or right
26
27        return dfs(root)
28
29        