# Last updated: 4/5/2026, 6:54:01 AM
1class Solution:
2    def judgeCircle(self, moves: str) -> bool:
3        u=0
4        d=0
5        l=0
6        r=0
7        for i in moves:
8            if i=='U':
9                u+=1
10            elif i=='D':
11                d+=1
12            elif i=='L':
13                l+=1
14            else:
15                r+=1
16        return r==l and u==d