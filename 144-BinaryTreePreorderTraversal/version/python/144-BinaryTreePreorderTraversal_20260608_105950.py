# Last updated: 6/8/2026, 10:59:50 AM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
9        if not root:
10            return []
11        res=[]
12        # def preorder(root):
13        #     if not root:
14        #         return
15        #     res.append(root.val)
16        #     preorder(root.left)
17        #     preorder(root.right)
18        # preorder(root)
19        # return res
20        stck=[root]
21        while stck:
22            head=stck.pop()
23            res.append(head.val)
24            if head.right:
25                stck.append(head.right)
26            if head.left:
27                stck.append(head.left)
28        return res
29
30
31