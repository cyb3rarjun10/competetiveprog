# Last updated: 3/14/2026, 9:56:10 AM
1class Solution:
2    def getHappyString(self, n: int, k: int) -> str:
3        happystr=[]
4        def genhappystr(s):
5            if len(s)==n:
6                happystr.append(s)
7                return
8            for i in {"a","b","c"}:
9                if s and s[-1]==i:
10                    continue
11                else:
12                    genhappystr(s+i)
13        genhappystr("")
14        happystr.sort()
15
16        if len(happystr)<k:
17            return ""
18        return happystr[k-1]