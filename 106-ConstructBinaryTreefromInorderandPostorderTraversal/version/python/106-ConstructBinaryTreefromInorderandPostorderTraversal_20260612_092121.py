# Last updated: 6/12/2026, 9:21:21 AM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
9        n=len(postorder)
10        d={}
11        for i in range(len(inorder)):
12            d[inorder[i]]=i
13        
14        def construct(po_idx,start,end):
15            if start>end:
16                return None
17            node=TreeNode(postorder[po_idx])
18            mid=d[node.val]
19
20            ls=start
21            le=mid-1
22
23            rs=mid+1
24            re=end
25
26            right_size=re-rs +1
27
28            node.right=construct(po_idx-1,rs,re)
29
30            node.left=construct(po_idx-right_size-1,ls,le)
31
32            return node
33
34        return construct(n-1,0,n-1)
35        
36
37            
38            