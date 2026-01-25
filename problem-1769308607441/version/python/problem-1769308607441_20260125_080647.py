# Last updated: 1/25/2026, 8:06:47 AM
1class Solution:
2    def minimumPrefixLength(self, nums: List[int]) -> int:
3        n=len(nums)
4        i=n-1
5        while n>=1:
6            if nums[i-1]<nums[i]:
7                i-=1
8            else:
9                break
10        move=n-i
11        return n-move