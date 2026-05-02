# Last updated: 5/2/2026, 7:14:52 PM
1class Solution:
2    def rotatedDigits(self, n: int) -> int:
3        dp = [0] * (n + 1)
4        count = 0
5
6        for i in range(n + 1):
7            if i < 10:
8                if i in (0, 1, 8):
9                    dp[i] = 1
10                elif i in (2, 5, 6, 9):
11                    dp[i] = 2
12                    count += 1
13                else:
14                    dp[i] = 0
15            else:
16                a = dp[i // 10]
17                b = dp[i % 10]
18
19                if a == 1 and b == 1:
20                    dp[i] = 1
21                elif a >= 1 and b >= 1:
22                    dp[i] = 2
23                    count += 1
24                else:
25                    dp[i] = 0
26
27        return count