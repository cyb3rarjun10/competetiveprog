# Last updated: 2/12/2026, 5:12:07 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
9        def buildtree(left,right):
10            if left>right:
11                return None
12            mid=(left+right)//2
13            root=TreeNode(nums[mid])
14            root.left=buildtree(left,mid-1)
15            root.right=buildtree(mid+1,right)
16            return root
17        return buildtree(0,len(nums)-1)
18