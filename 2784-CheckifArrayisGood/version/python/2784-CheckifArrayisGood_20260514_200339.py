# Last updated: 5/14/2026, 8:03:39 PM
1class Solution:
2    def isGood(self, nums: List[int]) -> bool:
3        nums.sort()
4        n = len(nums) - 1
5        for i in range(n):
6            if nums[i] != i + 1:
7                return False
8        return nums[n] == n