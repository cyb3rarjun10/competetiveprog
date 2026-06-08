# Last updated: 6/8/2026, 9:23:02 AM
1class Solution:
2    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
3        n=len(text1)
4        m=len(text2)
5        @cache
6        def dp(i,j):
7            if i==n or j==m:
8                return 0
9            if text1[i]==text2[j]:
10                return 1+dp(i+1,j+1)
11            p1=dp(i+1,j)
12            p2=dp(i,j+1)
13            return max(p2,p1)
14        return dp(0,0)
15        
16