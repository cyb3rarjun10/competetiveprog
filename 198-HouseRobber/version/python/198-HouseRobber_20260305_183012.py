# Last updated: 3/5/2026, 6:30:12 PM
1class Solution:
2    def rob(self, nums: List[int]) -> int:
3        n=len(nums)
4        @cache
5        def recurse(idx):
6            if idx>=n:
7                return 0
8            #rob
9            rob=nums[idx]+recurse(idx+2)
10            #skip
11            skip=recurse(idx+1)
12            return max(rob,skip)
13        return recurse(0)
14