# Last updated: 5/9/2026, 9:40:17 AM
1class Solution:
2    def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
3        m, n = len(grid), len(grid[0])
4        nlayer = min(m // 2, n // 2)  # level count
5        # enumerate each layer counterclockwise starting from the top-left corner
6        for layer in range(nlayer):
7            r = []  # row index of each element
8            c = []  # column index of each element
9            val = []  # value of each element
10            for i in range(layer, m - layer - 1):  # left
11                r.append(i)
12                c.append(layer)
13                val.append(grid[i][layer])
14            for j in range(layer, n - layer - 1):  # down
15                r.append(m - layer - 1)
16                c.append(j)
17                val.append(grid[m - layer - 1][j])
18            for i in range(m - layer - 1, layer, -1):  # right
19                r.append(i)
20                c.append(n - layer - 1)
21                val.append(grid[i][n - layer - 1])
22            for j in range(n - layer - 1, layer, -1):  # up
23                r.append(layer)
24                c.append(j)
25                val.append(grid[layer][j])
26            total = len(val)  # total number of elements in each layer
27            kk = k % total  # equivalent number of rotations
28            # find the value at each index after rotation
29            for i in range(total):
30                idx = (
31                    i + total - kk
32                ) % total  # the index corresponding to the value after rotation
33                grid[r[i]][c[i]] = val[idx]
34        return grid