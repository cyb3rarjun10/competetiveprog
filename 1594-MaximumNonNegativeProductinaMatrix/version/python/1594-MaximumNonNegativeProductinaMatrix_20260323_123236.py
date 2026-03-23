# Last updated: 3/23/2026, 12:32:36 PM
1class Solution:
2    def maxProductPath(self, grid: List[List[int]]) -> int:
3        mod = 10**9 + 7
4        m, n = len(grid), len(grid[0])
5        maxgt = [[0] * n for _ in range(m)]
6        minlt = [[0] * n for _ in range(m)]
7
8        maxgt[0][0] = minlt[0][0] = grid[0][0]
9        for i in range(1, n):
10            maxgt[0][i] = minlt[0][i] = maxgt[0][i - 1] * grid[0][i]
11        for i in range(1, m):
12            maxgt[i][0] = minlt[i][0] = maxgt[i - 1][0] * grid[i][0]
13
14        for i in range(1, m):
15            for j in range(1, n):
16                if grid[i][j] >= 0:
17                    maxgt[i][j] = (
18                        max(maxgt[i][j - 1], maxgt[i - 1][j]) * grid[i][j]
19                    )
20                    minlt[i][j] = (
21                        min(minlt[i][j - 1], minlt[i - 1][j]) * grid[i][j]
22                    )
23                else:
24                    maxgt[i][j] = (
25                        min(minlt[i][j - 1], minlt[i - 1][j]) * grid[i][j]
26                    )
27                    minlt[i][j] = (
28                        max(maxgt[i][j - 1], maxgt[i - 1][j]) * grid[i][j]
29                    )
30
31        if maxgt[m - 1][n - 1] < 0:
32            return -1
33        return maxgt[m - 1][n - 1] % mod