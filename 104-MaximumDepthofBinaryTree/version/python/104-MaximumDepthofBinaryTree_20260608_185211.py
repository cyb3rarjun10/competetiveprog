# Last updated: 6/8/2026, 6:52:11 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def maxDepth(self, root: Optional[TreeNode]) -> int:
9        if not root:
10            return 0
11        maxsteps=float('-inf')
12        def height(root):
13            if not root:
14                return 0
15            return 1+ max(height(root.left),height(root.right))
16        return height(root)