# Last updated: 4/13/2026, 6:46:14 PM
1class Solution:
2    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
3        minidx=float('inf')
4        for i in range(len(nums)):
5            if nums[i]==target:
6                minidx=min(minidx,abs(i-start))
7        return minidx