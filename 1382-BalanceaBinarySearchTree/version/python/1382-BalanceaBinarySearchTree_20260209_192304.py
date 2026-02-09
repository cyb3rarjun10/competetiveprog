# Last updated: 2/9/2026, 7:23:04 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
9        res=[]
10        def inorder(root):
11            if root is None:
12                return 
13            inorder(root.left)
14            res.append(root.val)
15            inorder(root.right)
16            
17        def construct(l,r):
18            if l>r:
19                return None
20            mid=(l+r)//2
21            newhead=TreeNode(res[mid])
22            newhead.left=construct(l,mid-1)
23            newhead.right=construct(mid+1,r)
24
25            return newhead
26        inorder(root)
27        return construct(0,len(res)-1)
28
29        
30
31
32