# Last updated: 6/10/2026, 10:49:39 AM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
9        
10        def issame(root1,root2):
11            if not root1 and not root2:
12                return True
13            if not root1 or not root2:
14                return False
15            if root1.val != root2.val:
16                return False
17            return issame(root1.left,root2.right ) and issame(root1.right,root2.left)
18
19        return issame(root,root)
20        