# Last updated: 3/8/2026, 8:44:38 AM
1class Solution:
2    def minOperations(self, s: str) -> int:
3        l=list(s)
4        if l==sorted(l):
5            return 0
6        if len(l)==2:
7            return -1
8        if max(l[:-1])<=l[-1]:
9            return 1
10        if min(l[1:])>=l[0]:
11            return 1
12        minchar=min(l)
13        maxchar=max(l)
14        if maxchar==l[0] and l.count(maxchar)==1 and l[-1]==minchar and l.count(minchar)==1:
15            return 3
16        return 2
17        