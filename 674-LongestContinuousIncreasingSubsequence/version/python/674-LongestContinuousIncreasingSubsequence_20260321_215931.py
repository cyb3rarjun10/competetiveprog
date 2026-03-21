# Last updated: 3/21/2026, 9:59:31 PM
1class Solution:
2    def findLengthOfLCIS(self, nums: List[int]) -> int:
3        n=len(nums)
4        l=0
5        res=0
6        r=1
7        while r<n:
8            if nums[r]<=nums[r-1]:
9                res=max(res,(r-l))
10                l=r
11            r+=1
12        return max(res,r-l)