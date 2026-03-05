# Last updated: 3/5/2026, 6:25:43 PM
1class Solution:
2    def rob(self, nums: List[int]) -> int:
3        n=len(nums)
4        maxcash=0
5        @cache
6        def recurse(idx,cash):
7            nonlocal maxcash
8            if idx>=n:
9                maxcash=max(maxcash,cash)
10                return 
11            #rob
12            recurse(idx+2,cash+nums[idx])
13            #skip
14            recurse(idx+1,cash)
15        recurse(0,0)
16        return maxcash
17