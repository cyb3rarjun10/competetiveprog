# Last updated: 3/6/2026, 6:33:22 PM
1class Solution:
2    def rob(self, nums: List[int], colors: List[int]) -> int:
3        n=len(nums)
4        @cache
5        def recurse(idx):
6            if idx>=n:
7                return 0
8            if idx+1<n:
9                if colors[idx]==colors[idx+1]:
10                    nxtidx=idx+2
11                else:
12                    nxtidx=idx+1
13            else:
14                nxtidx=idx+1
15            rob=nums[idx]+recurse(nxtidx)
16            skip=recurse(idx+1)
17            return max(rob,skip)
18        return recurse(0)
19        