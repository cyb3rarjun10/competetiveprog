# Last updated: 6/9/2026, 12:41:35 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
9        #queue->(node,row,col)
10        #moving left -> row+1, col-1
11        #moving right -> row+1, col+1
12        d=defaultdict(list)
13        stck=[(root,0,0)]
14        while stck:
15            curr,row,col=stck.pop()
16            d[(row,col)].append(curr.val)
17            if curr.right:
18                stck.append((curr.right,row+1,col+1))
19            if curr.left:
20                stck.append((curr.left,row+1,col-1))
21
22        orderdict = defaultdict(list)
23        
24        #Sort keys by Column index FIRST, then Row index SECOND
25        for (row, col) in sorted(d.keys(), key=lambda x: (x[1], x[0])):
26            # If multiple values exist at the exact same (row, col), sort them by value
27            sorted_values = sorted(d[(row, col)])
28            orderdict[col].extend(sorted_values)
29            
30        # Return the lists ordered from leftmost column to rightmost column
31        return [orderdict[c] for c in sorted(orderdict.keys())]
32
33
34        
35
36