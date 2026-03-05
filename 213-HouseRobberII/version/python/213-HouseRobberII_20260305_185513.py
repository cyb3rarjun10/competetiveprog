# Last updated: 3/5/2026, 6:55:13 PM
1class Solution:
2    def rob(self, nums: List[int]) -> int:
3        n=len(nums)
4        if n==1:
5            return nums[0]
6        @cache
7        def recurse(idx,n):
8            if idx>=n:
9                return 0
10            #rob
11            rob=nums[idx]+recurse(idx+2,n)
12            #skip
13            skip=recurse(idx+1,n)
14            return max(rob,skip)
15        x=recurse(0,n-1)
16        y=recurse(1,n)
17        return max(x,y)