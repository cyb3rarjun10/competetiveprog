# Last updated: 2/1/2026, 8:41:09 AM
1class Solution:
2    def finalElement(self, nums: List[int]) -> int:
3        return max(nums[0],nums[-1])