# Last updated: 3/28/2026, 4:50:23 PM
1class Solution:
2    def longestPalindrome(self, s: str) -> str:
3        n=len(s)
4        if n==1:
5            return s[-1]
6        d=defaultdict(list)
7        for i in range(n-1,-1,-1):
8            d[s[i]].append(i)
9        res=""
10        resl=float('-inf')
11        for l in range(n):
12            flag=True
13            for idx in d[s[l]]:
14                if not flag:
15                    continue
16                if l>idx:
17                    continue
18                r=idx
19                lp=l
20                rp=idx
21                while lp<=rp and s[lp]==s[rp]:
22                    lp+=1
23                    rp-=1
24                if lp>rp:
25                    flag=False
26                    temp=idx-l +1
27                    if temp>resl:
28                        res=s[l:idx+1]
29                        resl=temp
30        return res
31
32            