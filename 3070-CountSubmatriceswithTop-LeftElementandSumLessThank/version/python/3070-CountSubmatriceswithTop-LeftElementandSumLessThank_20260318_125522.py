# Last updated: 3/18/2026, 12:55:22 PM
1class Solution:
2    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
3        row=len(grid)
4        col=len(grid[0])
5        for i in range(row):
6            for j in range(col):
7                if j>0:
8                    grid[i][j]+=grid[i][j-1]
9        for i in range(row):
10            for j in range(col):
11                if i>0:
12                    grid[i][j]+=grid[i-1][j]
13        
14        res=0
15        print(grid)
16        for i in range(row):
17            for j in range(col):
18                if grid[i][j]<=k:
19                    res+=1
20        return res
21