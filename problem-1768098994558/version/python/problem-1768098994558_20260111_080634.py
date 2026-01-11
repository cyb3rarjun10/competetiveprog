# Last updated: 1/11/2026, 8:06:34 AM
1class Solution:
2    def residuePrefixes(self, s: str) -> int:
3        v=set()
4        prefixes=[]
5        n=len(s)
6        c=0
7        for i in s:
8            if i not in v:
9                c+=1
10            prefixes.append(c)
11            v.add(i)
12        res=0
13        for i in range(len(prefixes)):
14            if prefixes[i]==(i+1)%3:
15                res+=1
16        return res