# Last updated: 2/22/2026, 8:07:48 AM
1class Solution:
2    def scoreDifference(self, nums: List[int]) -> int:
3        n=len(nums)
4        fp=1
5        sp=-1
6        fps=0
7        sps=0
8        for i in range(n):
9            if (i+1)%6==0:
10                fp*=-1
11                sp*=-1
12            if nums[i]%2==1:
13                fp*=-1
14                sp*=-1
15            if fp==1:
16                fps+=nums[i]
17            if sp==1:
18                sps+=nums[i]
19        return fps-sps
20                