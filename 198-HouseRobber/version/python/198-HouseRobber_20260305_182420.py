# Last updated: 3/5/2026, 6:24:20 PM
1class Solution:
2    def rob(self, nums: List[int]) -> int:
3        n=len(nums)
4        @cache
5        def recurse(idx,cash):
6            if idx>=n:
7                return cash
8            #rob
9            x=recurse(idx+2,cash+nums[idx])
10            #skip
11            y=recurse(idx+1,cash)
12            return max(x,y)
13        return recurse(0,0)
14