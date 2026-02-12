# Last updated: 2/12/2026, 5:33:25 PM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6# Definition for a binary tree node.
7# class TreeNode:
8#     def __init__(self, val=0, left=None, right=None):
9#         self.val = val
10#         self.left = left
11#         self.right = right
12class Solution:
13    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
14        def buildtree(lp,rp):
15            if lp==rp:
16                return None
17            fp=lp
18            sp=lp
19            while fp!=rp and fp.next!=rp:
20                fp=fp.next.next
21                sp=sp.next
22            mid=sp
23            root=TreeNode(mid.val)
24            root.left=buildtree(lp,mid)
25            root.right=buildtree(mid.next,rp)
26            return root
27        return buildtree(head,None)
28