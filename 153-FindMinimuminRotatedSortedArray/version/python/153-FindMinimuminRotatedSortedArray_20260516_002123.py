# Last updated: 5/16/2026, 12:21:23 AM
1class Solution:
2    def findMin(self, nums: List[int]) -> int:
3        n=len(nums)
4        l=0
5        r=n-1
6        while l<r:
7            m=(l+r)//2
8            if nums[m] > nums[r]:
9                l=m+1
10            elif nums[m] < nums[r]:
11                r=m
12        return nums[l]