# Last updated: 6/9/2026, 9:19:56 AM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
9        if not root:
10            return []
11        queue=deque([root])
12        flag=1
13        res=[]
14        while queue:
15            l=len(queue)
16            temp=[]
17            for _ in range(l):
18                node=queue.popleft()
19                temp.append(node.val)
20                if node.left:
21                    queue.append(node.left)
22                if node.right:
23                    queue.append(node.right)
24            if flag==1:
25                res.append(temp)
26            elif flag==-1:
27                res.append(temp[::-1])
28            flag*=-1
29        return res
30
31