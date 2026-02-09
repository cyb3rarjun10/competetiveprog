# Last updated: 2/9/2026, 9:50:08 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def sumEvenGrandparent(self, root: Optional[TreeNode]) -> int:
9        tot=0
10        def recurse(curr,p,gp):
11            nonlocal tot
12            if curr is None:
13                return
14            if gp and gp.val%2==0:
15                tot+=curr.val
16            recurse(curr.left,curr,p)
17            recurse(curr.right,curr,p)
18        recurse(root,None,None)
19        return tot
20
21
22
23