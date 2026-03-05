# Last updated: 3/5/2026, 11:35:48 AM
1class Solution:
2    def minOperations(self, s: str) -> int:
3        res1=0
4        res2=0
5        n=len(s)
6        flag="0"
7        for i in range(n):
8            if s[i]!=flag:
9                res1+=1
10            if flag=="0":
11                flag="1"
12                continue
13            if flag=="1":
14                flag="0"
15        flag="1"
16        for i in range(n):
17            if s[i]!=flag:
18                res2+=1
19            if flag=="1":
20                flag="0"
21                continue
22            if flag=="0":
23                flag="1"
24        return min(res1,res2)
25