# Last updated: 6/13/2026, 3:11:35 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
9        if not root:
10            return 0
11            
12        max_width = 0
13        
14        queue = deque([(root, 1)])
15        
16        while queue:
17            level_length = len(queue)
18            
19            leftmost_idx = queue[0][1]
20            rightmost_idx = queue[-1][1]
21            
22            current_level_width = rightmost_idx - leftmost_idx + 1
23            max_width = max(max_width, current_level_width)
24            
25            # Process all nodes on the current level
26            for _ in range(level_length):
27                curr_node, x = queue.popleft()
28                
29                if curr_node.left:
30                    queue.append((curr_node.left, x * 2))
31                if curr_node.right:
32                    queue.append((curr_node.right, x * 2 + 1))
33                    
34        return max_width