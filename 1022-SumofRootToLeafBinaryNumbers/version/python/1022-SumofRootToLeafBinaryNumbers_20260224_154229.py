# Last updated: 2/24/2026, 3:42:29 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
9        rv=str(root.val)
10        stck=[(root,rv)]
11        tot=0
12        while stck:
13            currnode,bs=stck.pop()
14            if currnode.left==None and currnode.right==None:
15                tot+=int(bs,2)
16            if currnode.left:
17                vall=str(currnode.left.val)
18                stck.append((currnode.left,bs+vall))
19            if currnode.right:
20                vall=str(currnode.right.val)
21                stck.append((currnode.right,bs+vall))
22        return tot