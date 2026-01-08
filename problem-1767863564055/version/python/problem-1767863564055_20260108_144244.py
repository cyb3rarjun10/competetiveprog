# Last updated: 1/8/2026, 2:42:44 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
9        queue=deque([root])
10        recentsum=-1
11        while queue:
12            l=len(queue)
13            summ=0
14            for _ in range(l):
15                node=queue.popleft()
16                summ+=node.val
17                if node.left:
18                    queue.append(node.left)
19                if node.right:
20                    queue.append(node.right)
21            recentsum=summ
22        return recentsum
23                