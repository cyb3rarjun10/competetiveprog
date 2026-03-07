# Last updated: 3/7/2026, 5:37:03 PM
1class Solution:
2    def minFlips(self, s: str) -> int:
3        n=len(s)
4        s+=s
5        dp1=[0]*(2*n +1)
6        dp2=[0]*(2*n +1)
7        
8        for i in range(2*n):
9            target1="1" if i%2==0 else "0"
10            target2="0" if i%2==0 else "1"
11
12            dp1[i+1]=dp1[i]+(1 if s[i]!=target1 else 0)
13            dp2[i+1]=dp2[i]+(1 if s[i]!=target2 else 0)
14        
15        mincost=float('inf')
16        for i in range(n,2*n+1):
17            cost1=dp1[i]-dp1[i-n]
18            cost2=dp2[i]-dp2[i-n]
19            mincost=min(mincost,cost1,cost2)
20        return mincost
21
22
23
24