# Last updated: 3/22/2026, 7:19:23 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, x):
4#         self.val = x
5#         self.left = None
6#         self.right = None
7
8class Solution:
9    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
10        def dfs(root):
11            if not root or root==p or root==q:
12                return root
13            left=dfs(root.left)
14            right=dfs(root.right)
15            if not left:
16                return right
17            elif not right:
18                return left
19            else: return root
20        return dfs(root)
21            
22            
23