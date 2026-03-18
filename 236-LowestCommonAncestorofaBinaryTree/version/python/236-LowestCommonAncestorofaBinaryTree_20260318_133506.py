# Last updated: 3/18/2026, 1:35:06 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, x):
4#         self.val = x
5#         self.left = None
6#         self.right = None
7
8class Solution:
9    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
10        queue=deque([root])
11        parent={}
12        depth={}
13        level=0
14        while queue:
15            l=len(queue)
16            for _ in range(l):
17                curr=queue.popleft()
18                depth[curr]=level
19                if curr.left:
20                    queue.append(curr.left)
21                    parent[curr.left]=curr
22                if curr.right:
23                    queue.append(curr.right)
24                    parent[curr.right]=curr
25            level+=1
26        
27        while depth[p]<depth[q]:
28            q=parent[q]
29        while depth[p]>depth[q]:
30            p=parent[p]
31            
32        while p!=q:
33            p=parent[p]
34            q=parent[q]
35        return p
36        
37
38