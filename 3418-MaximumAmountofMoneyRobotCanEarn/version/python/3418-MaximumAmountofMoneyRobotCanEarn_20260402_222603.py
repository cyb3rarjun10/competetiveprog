# Last updated: 4/2/2026, 10:26:03 PM
1class Solution:
2    def maximumAmount(self,coins: List[List[int]]) -> int:
3        r, c = len(coins), len(coins[0])
4        dp = [[[-float('inf')] * 3 for _ in range(c)] for _ in range(r)]
5    
6        for k in range(3):
7            if coins[0][0] < 0 and k > 0:
8                dp[0][0][k] = 0
9            else:
10                dp[0][0][k] = coins[0][0]
11    
12        for i in range(r):
13            for j in range(c):
14                for k in range(3):
15                    if i == 0 and j == 0:
16                        continue
17                    val = coins[i][j]
18                    if val < 0:
19                        if i > 0:
20                            dp[i][j][k] = max(dp[i][j][k], dp[i-1][j][k] + val)
21                        if j > 0:
22                            dp[i][j][k] = max(dp[i][j][k], dp[i][j-1][k] + val)
23                        if k > 0:
24                            if i > 0:
25                                dp[i][j][k] = max(dp[i][j][k], dp[i-1][j][k-1])
26                            if j > 0:
27                                dp[i][j][k] = max(dp[i][j][k], dp[i][j-1][k-1])
28                    else:
29                        if i > 0:
30                            dp[i][j][k] = max(dp[i][j][k], dp[i-1][j][k] + val)
31                        if j > 0:
32                            dp[i][j][k] = max(dp[i][j][k], dp[i][j-1][k] + val)
33     
34        return max(dp[r-1][c-1])
35
36    
37
38