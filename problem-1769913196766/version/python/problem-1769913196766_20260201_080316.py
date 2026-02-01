# Last updated: 2/1/2026, 8:03:16 AM
1class Solution:
2    def countMonobit(self, n: int) -> int:
3        c=0
4        for i in range(n+1):
5            b=bin(i)
6            s=set(b[2:])
7            if len(s)==1:
8                c+=1
9        return c