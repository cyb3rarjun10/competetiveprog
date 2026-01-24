# Last updated: 1/24/2026, 6:18:55 PM
1class Solution:
2    def minPairSum(self, nums: List[int]) -> int:
3        nums.sort()
4        n=len(nums)
5        maxpair=float('-inf')
6        for i in range(n//2):
7            summ=nums[i]+nums[n-1-i]
8            maxpair=max(maxpair,summ)
9        return maxpair