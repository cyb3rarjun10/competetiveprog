# Last updated: 3/6/2026, 9:09:10 PM
1class Solution:
2    def numDecodings(self, s: str) -> int:
3        n=len(s)
4        #bottomup (tabulation)
5        # dp=[0]*(n+1)
6        # dp[0]=1
7        # if s[0]=="0":
8        #     dp[1]=0
9        # else:
10        #     dp[1]=1
11        # for i in range(2,n+1):
12        #     if s[i-1]!="0":
13        #         dp[i]=dp[i-1]
14        #     if 10<=int(s[i-2:i])<=26:
15        #         dp[i]+=dp[i-2]
16        # return dp[n]
17        back2=1 
18        back1=0 if s[0]=="0" else 1
19        for i in range(2,n+1):
20            curr=0
21            if s[i-1]!="0":
22                curr=back1
23            if 10<=int(s[i-2:i])<=26:
24                curr+=back2
25            back2=back1
26            back1=curr
27        return back1
28
29
30
31