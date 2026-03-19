# Last updated: 3/19/2026, 5:04:50 PM
1class Solution:
2    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
3        row = len(grid)
4        col = len(grid[0])
5
6        # convert to 0/1
7        mat = [[1 if grid[i][j] == "X" else 0 for j in range(col)] for i in range(row)]
8
9        # row prefix
10        for i in range(row):
11            for j in range(col):
12                if j > 0:
13                    mat[i][j] += mat[i][j-1]
14
15        # column prefix
16        for i in range(row):
17            for j in range(col):
18                if i > 0:
19                    mat[i][j] += mat[i-1][j]
20
21        # convert to 0/1
22        mat1 = [[1 if grid[i][j] == "Y" else 0 for j in range(col)] for i in range(row)]
23
24        # row prefix
25        for i in range(row):
26            for j in range(col):
27                if j > 0:
28                    mat1[i][j] += mat1[i][j-1]
29
30        # column prefix
31        for i in range(row):
32            for j in range(col):
33                if i > 0:
34                    mat1[i][j] += mat1[i-1][j]
35        res=0
36        for i in range(row):
37            for j in range(col):
38                if mat1[i][j]==mat[i][j] and mat[i][j]!=0:
39                    res+=1
40        return res
41
42
43        