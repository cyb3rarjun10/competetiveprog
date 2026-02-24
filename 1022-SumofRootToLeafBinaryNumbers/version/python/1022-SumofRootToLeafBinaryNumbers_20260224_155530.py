# Last updated: 2/24/2026, 3:55:30 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
9        res=0
10        def dfs(root,bs):
11            nonlocal res
12            if root.left ==None and root.right==None:
13                if bs!="":
14                    res+=int(bs,2)
15                return
16            if root.left:
17                dfs(root.left,bs+str(root.left.val))
18            if root.right:
19                dfs(root.right,bs+str(root.right.val))
20        dfs(root,str(root.val))
21        return res
22