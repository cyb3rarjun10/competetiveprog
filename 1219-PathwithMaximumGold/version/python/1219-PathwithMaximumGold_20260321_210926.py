# Last updated: 3/21/2026, 9:09:26 PM
1class Solution:
2    def getMaximumGold(self, grid: List[List[int]]) -> int:
3        row = len(grid)
4        col = len(grid[0])
5        directions = [(0, -1), (0, 1), (1, 0), (-1, 0)]      
6        def recurse(cr, cc, v):
7            temp = []
8            for dr, dc in directions:
9                nr, nc = cr + dr, cc + dc
10                if 0 <= nr < row and 0 <= nc < col and grid[nr][nc] != 0 and (nr, nc) not in v:
11                    v.add((nr, nc))
12                    goldcollected = recurse(nr, nc, v)
13                    temp.append(goldcollected)
14                    v.remove((nr, nc))
15            return grid[cr][cc] + (max(temp) if temp else 0)
16            
17        res = 0
18        for i in range(row):
19            for j in range(col):
20                if grid[i][j] != 0:
21                    x = recurse(i, j, {(i, j)})
22                    res = max(res, x)
23                    
24        return res