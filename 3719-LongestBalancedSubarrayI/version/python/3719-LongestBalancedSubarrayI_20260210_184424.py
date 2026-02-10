# Last updated: 2/10/2026, 6:44:24 PM
1class Solution:
2    def longestBalanced(self, nums: List[int]) -> int:
3        n=len(nums)
4        result=0
5        for l in range(n):
6            seen, B = set(), 0
7            for r in range(l, n):
8                x = nums[r]
9                if x not in seen:
10                    seen.add(x)
11                    B += 1 if (x % 2) == 0 else -1
12                if B == 0:
13                    result = max(result, r - l + 1)
14        return result