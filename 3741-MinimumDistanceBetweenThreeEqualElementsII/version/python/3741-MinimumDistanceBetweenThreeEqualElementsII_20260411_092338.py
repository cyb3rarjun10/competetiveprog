# Last updated: 4/11/2026, 9:23:38 AM
1class Solution:
2    def minimumDistance(self, nums: List[int]) -> int:
3        d=defaultdict(list)
4        for i in range(len(nums)):
5            d[nums[i]].append(i)
6
7        dist=float('inf')
8        for ind in d.values():
9            if len(ind)<3:
10                continue
11            for i in range(len(ind)-2):
12                dist=min(dist, 2*(ind[i+2]-ind[i]))
13        return dist if dist!=float('inf') else -1
14
15        