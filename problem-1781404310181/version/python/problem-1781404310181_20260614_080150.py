# Last updated: 6/14/2026, 8:01:50 AM
1class Solution:
2    def checkGoodInteger(self, n: int) -> bool:
3        s=str(n)
4        dsum=0
5        ssum=0
6        for i in s:
7            dsum+=int(i)
8            ssum+=int(i)*int(i)
9        return ssum-dsum >=50