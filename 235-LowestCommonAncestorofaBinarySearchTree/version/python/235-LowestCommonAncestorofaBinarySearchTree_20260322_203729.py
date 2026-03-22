# Last updated: 3/22/2026, 8:37:29 PM
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
11            
12            if p.val<root.val and q.val <root.val:
13                return dfs(root.left)
14                
15            elif p.val>root.val and q.val>root.val:
16                return dfs(root.right)
17                
18            else:
19                return root
20        return dfs(root)