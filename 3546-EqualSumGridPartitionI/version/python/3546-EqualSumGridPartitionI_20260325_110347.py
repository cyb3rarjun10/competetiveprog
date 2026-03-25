# Last updated: 3/25/2026, 11:03:47 AM
1class Solution:
2    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
3        totalsum=0
4        row= len(grid)
5        col=len(grid[0])
6        for r in range(row):
7            for c in range(col):
8                totalsum+=grid[r][c]
9        if totalsum%2!=0:
10            return False
11        res=0
12        #vertical
13        for r in range(row-1):
14            s=0
15            for c in range(col):
16                s+=grid[r][c]
17            res+=s
18
19            if res==totalsum//2:
20                return True
21        res=0
22        #horizontal
23        for c in range(col-1):
24            s=0
25            for r in range(row):
26                s+=grid[r][c]
27            res+=s
28            if res==totalsum//2:
29                return True
30        return False
31                
32        
33
34
35