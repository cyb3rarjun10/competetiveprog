# Last updated: 4/17/2026, 3:49:21 PM
1class Solution:
2    def minMirrorPairDistance(self, nums: List[int]) -> int:
3        def reverse(x):
4            return int(str(x)[::-1])
5        d={}
6        mindist=float('inf')
7        n=len(nums)
8        for i in range(n):
9            r=reverse(nums[i])
10            if nums[i] in d:
11                mindist=min(mindist, abs(i-d[nums[i]]))
12            d[r]=i
13        if mindist==float('inf'):
14            return -1
15        return mindist