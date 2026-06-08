# Last updated: 6/8/2026, 1:17:46 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def isBalanced(self, root: Optional[TreeNode]) -> bool:
9
10        def height(node):
11            if not node:
12                return 0
13
14            return 1 + max(height(node.left), height(node.right))
15
16        def balanced(node):
17            if not node:
18                return True
19
20            lh = height(node.left)
21            rh = height(node.right)
22
23            if abs(lh - rh) > 1:
24                return False
25
26            return balanced(node.left) and balanced(node.right)
27
28        return balanced(root)