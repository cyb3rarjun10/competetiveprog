# Last updated: 3/6/2026, 9:05:12 AM
1class Solution:
2    def checkOnesSegment(self, s: str) -> bool:
3        c=0
4        n=len(s)
5        i=0
6        while i<n:
7            if s[i]=="1":
8                j=i
9                while j<n and s[j]=="1":
10                    j+=1
11                c+=1
12                i=j
13            else:
14                i+=1
15        return c==1