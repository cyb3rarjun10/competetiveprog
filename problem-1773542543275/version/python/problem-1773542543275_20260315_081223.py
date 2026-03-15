# Last updated: 3/15/2026, 8:12:23 AM
1class Solution:
2    def countCommas(self, n: int) -> int:
3        if n < 1000:
4            return 0
5        tc= 0
6        for i in range(1000, n +1):
7            tc +=len(str(i))// 3 -(1 if len(str(i))% 3==0 else 0)
8        return tc
9        