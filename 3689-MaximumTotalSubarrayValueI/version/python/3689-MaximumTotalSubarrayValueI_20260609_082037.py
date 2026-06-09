# Last updated: 6/9/2026, 8:20:37 AM
1class Solution:
2    def maxTotalValue(self, nums: List[int], k: int) -> int:
3        if nums==[]:
4            return 0
5        mm=min(nums)
6        ma=max(nums)
7        val=ma-mm
8        return val*k
9