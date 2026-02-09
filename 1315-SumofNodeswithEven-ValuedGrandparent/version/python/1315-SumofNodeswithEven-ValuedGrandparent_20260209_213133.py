# Last updated: 2/9/2026, 9:31:33 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def sumEvenGrandparent(self, root: Optional[TreeNode]) -> int:
9        queue=deque([(root,None,None)]) #(root,parent,grandparent)
10        tot=0
11        while queue:
12            curr,p,gp=queue.popleft()
13            if gp!=None and gp.val %2==0:
14                tot+=curr.val
15            if curr.left:
16                queue.append((curr.left,curr,p))
17            if curr.right:
18                queue.append((curr.right,curr,p))
19        return tot
20
21