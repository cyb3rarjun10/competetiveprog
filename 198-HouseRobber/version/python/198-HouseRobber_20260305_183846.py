# Last updated: 3/5/2026, 6:38:46 PM
1class Solution:
2    def rob(self, nums: List[int]) -> int:
3        n=len(nums)
4        if n==1:
5            return nums[0]
6        dp=[0]*n
7        dp[0]=nums[0]
8        dp[1]=max(nums[0],nums[1])
9        for i in range(2,n):
10            rob=nums[i]+dp[i-2]
11            skip=dp[i-1]
12            dp[i]=max(rob,skip)
13        return dp[n-1]
14