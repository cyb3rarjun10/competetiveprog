# Last updated: 3/23/2026, 12:46:51 PM
1class Solution:
2    def maxProductPath(self, grid: List[List[int]]) -> int:
3        mod = 10**9 + 7
4        row,col = len(grid), len(grid[0])
5        @cache
6        def dfs(r,c):
7            if r==row-1 and c==col-1:
8                return (grid[r][c],grid[r][c])
9            minprod=float('inf')
10            maxprod=float('-inf')
11            if c+1<col:
12                rmin,rmax=dfs(r,c+1)
13                p1=grid[r][c]*rmin
14                p2=grid[r][c]*rmax
15                minprod=min(p1,p2,minprod)
16                maxprod=max(p1,p2,maxprod)
17            if r+1<row:
18                dmin,dmax=dfs(r+1,c)
19                p1=grid[r][c]*dmin
20                p2=grid[r][c]*dmax
21                minprod=min(p1,p2,minprod)
22                maxprod=max(p1,p2,maxprod)
23            return minprod,maxprod
24        minp,maxp=dfs(0,0)
25        if maxp<0:
26            return -1
27        return maxp%mod