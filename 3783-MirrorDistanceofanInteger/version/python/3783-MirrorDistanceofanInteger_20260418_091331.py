# Last updated: 4/18/2026, 9:13:31 AM
1class Solution:
2    def mirrorDistance(self, n: int) -> int:
3        s=str(n)
4        rev=s[::-1]
5        return abs(n-int(rev))