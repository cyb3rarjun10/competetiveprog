# Last updated: 6/10/2026, 9:22:55 AM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
9        if not root:
10            return []
11        d=defaultdict(int)
12        stck=[(0,0,root)]
13        while stck:
14            row,col,curr=stck.pop()
15            if (row,col) not in d:
16                d[(row,col)]=curr.val
17            if curr.left:
18                stck.append((row+1,col-1,curr.left))
19            if curr.right:
20                stck.append((row+1,col+1,curr.right))
21        
22        resdict={}
23        for (row,col), value in sorted(d.items(),key=lambda item:item[0][0]):
24            print
25            if row not in resdict:
26                resdict[row]=value
27        res=[]
28        for key in resdict:
29            res.append(resdict[key])
30        return res
31        
32