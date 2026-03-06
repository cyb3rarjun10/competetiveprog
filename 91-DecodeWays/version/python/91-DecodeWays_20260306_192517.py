# Last updated: 3/6/2026, 7:25:17 PM
1class Solution:
2    def numDecodings(self, s: str) -> int:
3        n=len(s)
4        @cache
5        def recurse(idx):
6            if idx>=n:
7                return 1
8            if s[idx]=="0":
9                return 0
10            step1=recurse(idx+1)
11            if 10<=int(s[idx:idx+2])<=26:
12                step2=recurse(idx+2)
13            else:
14                step2=0
15            return step1+step2
16        return recurse(0)
17            
18
19