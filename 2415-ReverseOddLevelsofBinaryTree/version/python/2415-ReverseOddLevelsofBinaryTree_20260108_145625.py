# Last updated: 1/8/2026, 2:56:25 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7
8class Solution:
9    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
10        if not root:
11            return None
12        
13        queue = deque([root])
14        lvl = 0
15        
16        while queue:
17            size = len(queue)
18            level_nodes = []
19            
20            # Collect all nodes at this level
21            for _ in range(size):
22                node = queue.popleft()
23                level_nodes.append(node)
24                
25                if node.left:
26                    queue.append(node.left)
27                if node.right:
28                    queue.append(node.right)
29            
30            # Reverse values if level is odd
31            if lvl % 2 == 1:
32                vals = [node.val for node in level_nodes][::-1]  # reversed values
33                for node, val in zip(level_nodes, vals):
34                    node.val = val
35            
36            lvl += 1
37        
38        return root
39
40        
41            
42