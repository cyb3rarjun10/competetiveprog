# Last updated: 6/8/2026, 6:49:37 PM
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
12        def recurse(curr,steps):
13            nonlocal maxsteps
14            if not curr:
15                return 
16
17            if not curr.left and not curr.right:
18                maxsteps=max(maxsteps,steps)
19                return
20            
21            if curr.left:
22                recurse(curr.left,steps+1)
23            if curr.right:
24                recurse(curr.right,steps+1)
25        
26        recurse(root,1)
27        return maxsteps