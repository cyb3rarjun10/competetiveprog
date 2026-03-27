# Last updated: 3/27/2026, 2:03:26 PM
1class Solution:
2    def findTargetSumWays(self, nums: List[int], target: int) -> int:
3        n = len(nums)
4
5        @cache
6        def recurse(idx, currsum):
7            if idx == n:
8                return 1 if currsum == target else 0
9
10            return (
11                recurse(idx + 1, currsum + nums[idx]) +
12                recurse(idx + 1, currsum - nums[idx])
13            )
14
15        return recurse(0, 0)