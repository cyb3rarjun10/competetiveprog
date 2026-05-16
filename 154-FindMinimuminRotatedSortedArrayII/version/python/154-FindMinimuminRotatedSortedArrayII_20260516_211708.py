# Last updated: 5/16/2026, 9:17:08 PM
1class Solution:
2    def findMin(self, nums: List[int]) -> int:
3        while len(nums) > 1 and nums[-1] == nums[0]:
4            nums.pop()
5
6        return nums[bisect_left(nums, True, key=lambda n: n <= nums[-1])]