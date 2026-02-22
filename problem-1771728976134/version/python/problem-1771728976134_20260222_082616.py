# Last updated: 2/22/2026, 8:26:16 AM
1class Solution:
2    def maximumXor(self, s: str, t: str) -> str:
3        n=len(s)
4        remzero=0
5        remone=0
6        for i in t:
7            if i=="0":
8                remzero+=1
9            else:
10                remone+=1
11        newbin=""
12        for i in s:
13            if i=="1":
14                if remzero>0:
15                    remzero-=1
16                    newbin+="1"
17                else:
18                    remone-=1
19                    newbin+="0"
20            else:
21                if remone>0:
22                    remone-=1
23                    newbin+="1"
24                else:
25                    remzero-=1
26                    newbin+="0"
27        return newbin
28        