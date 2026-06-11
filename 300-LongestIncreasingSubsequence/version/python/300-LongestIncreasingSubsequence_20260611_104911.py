# Last updated: 6/11/2026, 10:49:11 AM
1class Solution:
2    def lengthOfLIS(self, nums: List[int]) -> int:
3        n = len(nums)
4
5        #lis starting from index i (state)
6        @cache
7        def dp(i):
8            best = 1
9
10            for nxt in range(i + 1, n):
11                if nums[nxt] > nums[i]:
12                    best = max(best, 1 + dp(nxt))
13
14            return best
15
16        ans = 0
17        for i in range(n):
18            ans = max(ans, dp(i))
19
20        return ans
21