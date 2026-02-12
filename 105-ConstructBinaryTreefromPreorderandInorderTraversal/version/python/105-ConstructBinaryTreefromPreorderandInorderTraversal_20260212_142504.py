# Last updated: 2/12/2026, 2:25:04 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
9        n=len(inorder)
10        d={}
11        for i in range(n):
12            d[inorder[i]]=i
13        preidx=0
14        def buildtree(left,right):
15            nonlocal preidx
16            if left>right:
17                return None
18            root=TreeNode(preorder[preidx])
19            idx=d[preorder[preidx]]
20            preidx+=1
21            root.left=buildtree(left,idx-1)
22            root.right=buildtree(idx+1,right)
23            return root
24        return buildtree(0,len(inorder)-1)
25
26            
27