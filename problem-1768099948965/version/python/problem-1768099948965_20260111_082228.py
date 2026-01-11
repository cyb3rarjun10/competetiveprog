# Last updated: 1/11/2026, 8:22:28 AM
1class Solution:
2    def centeredSubarrays(self, nums: List[int]) -> int:
3        n=len(nums)
4        res=0
5        for i in range(n):
6            currsum=0
7            v=set()
8            for j in range(i,n):
9                currsum+=nums[j]
10                v.add(nums[j])
11                if currsum in v:
12                    res+=1
13        return res