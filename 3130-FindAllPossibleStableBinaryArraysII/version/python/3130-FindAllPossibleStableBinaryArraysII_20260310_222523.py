# Last updated: 3/10/2026, 10:25:23 PM
1class Solution:
2    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
3        mod = 10**9 + 7
4
5        dp = [[[0, 0] for _ in range(one + 1)] for _ in range(zero + 1)]
6        for i in range(zero + 1):
7            for j in range(one + 1):
8                for lastBit in range(2):
9                    if i == 0:
10                        if lastBit == 0 or j > limit:
11                            dp[i][j][lastBit] = 0
12                        else:
13                            dp[i][j][lastBit] = 1
14                    elif j == 0:
15                        if lastBit == 1 or i > limit:
16                            dp[i][j][lastBit] = 0
17                        else:
18                            dp[i][j][lastBit] = 1
19                    elif lastBit == 0:
20                        dp[i][j][lastBit] = dp[i - 1][j][0] + dp[i - 1][j][1]
21                        if i > limit:
22                            dp[i][j][lastBit] -= dp[i - limit - 1][j][1]
23                    else:
24                        dp[i][j][lastBit] = dp[i][j - 1][0] + dp[i][j - 1][1]
25                        if j > limit:
26                            dp[i][j][lastBit] -= dp[i][j - limit - 1][0]
27                    dp[i][j][lastBit] %= mod
28        return (dp[-1][-1][0] + dp[-1][-1][1]) % mod