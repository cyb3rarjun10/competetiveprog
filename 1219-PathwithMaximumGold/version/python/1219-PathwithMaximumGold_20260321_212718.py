# Last updated: 3/21/2026, 9:27:18 PM
1class Solution:
2    def getMaximumGold(self, grid: List[List[int]]) -> int:
3        row = len(grid)
4        col = len(grid[0])
5        directions = [(0, -1), (0, 1), (1, 0), (-1, 0)]      
6        def recurse(cr, cc, v):
7            goldcollected=0
8            for dr, dc in directions:
9                nr, nc = cr + dr, cc + dc
10                if 0 <= nr < row and 0 <= nc < col and grid[nr][nc] != 0 and (nr, nc) not in v:
11                    v.add((nr, nc))
12                    goldcollected = max(goldcollected,recurse(nr, nc, v))
13                    v.remove((nr, nc))
14            return grid[cr][cc] + goldcollected
15            
16        res = 0
17        for i in range(row):
18            for j in range(col):
19                if grid[i][j] != 0:
20                    x = recurse(i, j, {(i, j)})
21                    res = max(res, x)
22                    
23        return res