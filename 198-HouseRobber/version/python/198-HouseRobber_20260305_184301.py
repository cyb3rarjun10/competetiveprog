# Last updated: 3/5/2026, 6:43:01 PM
1class Solution:
2    def rob(self, nums: List[int]) -> int:
3        n=len(nums)
4        if n==1:
5            return nums[0]
6        rob0=nums[0]
7        rob1=max(nums[0],nums[1])
8        for i in range(2,n):
9            rob=nums[i]+rob0
10            skip=rob1
11            rob0=rob1
12            rob1=max(rob,skip)
13
14        return rob1
15