# Last updated: 3/28/2026, 8:34:52 PM
1class Solution:
2    def minCost(self, grid: list[list[int]]) -> int:
3        row=len(grid)
4        col=len(grid[0])
5        stck=[(0,0,grid[0][0])]
6        res=float('inf')
7        v=set()
8        while stck:
9            cr,cc,curr=stck.pop()
10            if cr==row-1 and cc==col-1:
11                res=min(res,curr)
12                continue
13            if (cr,cc,curr) in v:
14                continue
15            v.add((cr,cc,curr))
16            if cc+1<col:
17                stck.append((cr,cc+1,curr^grid[cr][cc+1]))
18            if cr+1<row:
19                stck.append((cr+1,cc,curr^grid[cr+1][cc]))
20        return res
21                