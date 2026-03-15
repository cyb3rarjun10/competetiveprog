# Last updated: 3/15/2026, 8:26:08 AM
1class Solution:
2    def countCommas(self, n: int) -> int:
3        if n<1000:
4            return 0
5        grp=1000
6        c=0
7        while n>=grp:
8            c+=(n-grp)+1
9            grp*=1000
10        return c
11        
12            