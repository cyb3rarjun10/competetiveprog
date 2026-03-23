# Last updated: 3/23/2026, 6:52:38 PM
1class Solution:
2    def minPathSum(self, grid: List[List[int]]) -> int:
3        row=len(grid)
4        col=len(grid[0])
5        dp=[[0]*col]*row
6        dp[0][0]=grid[0][0]
7        for r in range(row):
8            for c in range(col):
9                if r==0 and c==0:
10                    continue
11                toppath=float('inf')
12                leftpath=float('inf')
13                topr,topc=r-1,c
14                leftr,leftc=r,c-1
15                
16                if 0<=topr<row and 0<=topc<col:
17                    toppath=dp[topr][topc]
18                if 0<=leftr<row and 0<=leftc<col:
19                    leftpath=dp[leftr][leftc]
20                dp[r][c]=min(toppath,leftpath)+grid[r][c]
21        return dp[row-1][col-1]
22                
23
24