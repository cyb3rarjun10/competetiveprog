# Last updated: 3/22/2026, 8:37:45 AM
1class Solution:
2    def minRemovals(self, nums: List[int], target: int) -> int:
3        n=len(nums)
4        @cache
5        def recurse(idx,curr):
6            if idx==n:
7                if curr==target:
8                    return 0
9                else:
10                    return float('inf')
11            #take
12            take=recurse(idx+1,curr^nums[idx])
13            #dont take
14            skip=1+recurse(idx+1,curr)
15            return min(take,skip)
16        x=recurse(0,0)
17        if x==float('inf'):
18            return -1
19        return x