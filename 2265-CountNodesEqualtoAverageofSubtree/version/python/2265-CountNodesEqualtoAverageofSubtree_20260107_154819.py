# Last updated: 1/7/2026, 3:48:19 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def averageOfSubtree(self, root: TreeNode) -> int:
9        res=0
10        def matchcount(node):
11            nonlocal res
12            if node is None:
13                return 0,0
14            leftsubtree=matchcount(node.left)
15            rightsubtree=matchcount(node.right)
16
17            summ=leftsubtree[0]+rightsubtree[0] + node.val
18            count=leftsubtree[1]+rightsubtree[1]+1
19            
20            if summ//count == node.val:
21                res+=1
22            return summ,count
23        matchcount(root)
24        return res