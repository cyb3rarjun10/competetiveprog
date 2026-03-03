# Last updated: 3/3/2026, 9:27:12 PM
1class Solution:
2    def canJump(self, nums: List[int]) -> bool:
3        n=len(nums)
4        maxreach=0
5        for i in range(n):
6            if maxreach>=n-1:
7                return True
8            if i>maxreach:
9                return False
10            maxreach=max(maxreach,i+nums[i])