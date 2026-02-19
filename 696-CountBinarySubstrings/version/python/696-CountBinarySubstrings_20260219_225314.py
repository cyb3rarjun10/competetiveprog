# Last updated: 2/19/2026, 10:53:14 PM
1class Solution:
2    def countBinarySubstrings(self, s: str) -> int:
3        n=len(s)
4        i=0
5        res=[]
6        while i<n:
7            oc=0
8            while i<n and s[i]=="1":
9                i+=1
10                oc+=1
11            if oc!=0:
12                res.append(oc)
13            zc=0
14            while i<n and s[i]=="0":
15                i+=1
16                zc+=1
17            if zc!=0:
18                res.append(zc)
19        subs=0
20        for i in range(len(res)-1):
21            subs+=min(res[i],res[i+1])
22        return subs
23
24