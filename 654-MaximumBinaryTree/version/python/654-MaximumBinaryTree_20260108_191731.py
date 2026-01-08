# Last updated: 1/8/2026, 7:17:31 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
9        def construction(arr):
10            if not arr:
11                return None
12            m=max(arr)
13            idx=arr.index(m)
14            root=TreeNode(m)
15            leftsubtree=construction(arr[:idx])
16            rightsubtree=construction(arr[idx+1:])
17            root.left=leftsubtree
18            root.right=rightsubtree
19            return root
20        return construction(nums)
21
22