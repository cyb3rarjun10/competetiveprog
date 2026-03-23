# Last updated: 3/23/2026, 12:23:18 PM
1class Solution:
2    def maxProductPath(self, grid: List[List[int]]) -> int:
3        mod=(10**9)+7
4        row=len(grid)
5        col=len(grid[0])
6        directions=[(0,1),(1,0)]
7        maxprod=float('-inf')
8        @cache
9        def dfs(r,c,curr):
10            nonlocal maxprod
11            if r==row-1 and c==col-1:
12                maxprod=max(maxprod,curr)
13                return 
14            for dr,dc in directions:
15                nr,nc=r+dr,c+dc
16                if 0<=nr<row and 0<=nc<col:
17                    dfs(nr,nc,curr*grid[nr][nc])
18        dfs(0,0,grid[0][0])
19        return maxprod%mod if maxprod>=0 else -1