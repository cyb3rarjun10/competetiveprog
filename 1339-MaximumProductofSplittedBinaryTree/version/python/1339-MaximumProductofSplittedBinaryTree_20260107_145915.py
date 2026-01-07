# Last updated: 1/7/2026, 2:59:15 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def maxProduct(self, root: Optional[TreeNode]) -> int:
9        stck=[root]
10        totsum=0
11        while stck:
12            curr=stck.pop()
13            totsum+=curr.val
14            if curr.left:
15                stck.append(curr.left)
16            if curr.right:
17                stck.append(curr.right)
18        maxprod=0
19        def postorder(root):
20            nonlocal maxprod
21            if not root:
22                return 0
23            leftsum=postorder(root.left)
24            rightsum=postorder(root.right)
25
26            subarrsum=root.val + leftsum+rightsum
27
28            prod=(totsum-subarrsum)*subarrsum
29            maxprod=max(maxprod,prod)
30            return subarrsum
31        postorder(root)
32        return maxprod % (10**9 +7)