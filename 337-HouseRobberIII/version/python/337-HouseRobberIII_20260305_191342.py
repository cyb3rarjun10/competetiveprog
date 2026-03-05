# Last updated: 3/5/2026, 7:13:42 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def rob(self, root: Optional[TreeNode]) -> int:
9        @cache
10        def recurse(curr):
11            if curr is None:
12                return 0
13            if curr.left and curr.right:
14                rob=curr.val + recurse(curr.left.left) + recurse(curr.left.right) + recurse(curr.right.left) + recurse(curr.right.right)
15            elif curr.left:
16                rob=curr.val + recurse(curr.left.left) + recurse(curr.left.right) 
17            elif curr.right:
18                rob=curr.val + recurse(curr.right.left) + recurse(curr.right.right)
19            else:
20                rob=curr.val
21            skip=recurse(curr.left)+recurse(curr.right)
22            return max(rob,skip)
23        return recurse(root)