# Last updated: 3/24/2026, 12:53:49 PM
1class Solution:
2    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
3        m=10**5
4        mod=12345
5        row=len(grid)
6        col=len(grid[0])
7        res=[[1 for i in range(col)]for j in range(row)]
8        prefixprod=[[1 for i in range(col)] for j in range(row)]
9        suffixprod=[[1 for i in range(col)] for j in range(row)]
10        preprod=1
11        sufprod=1
12        for r in range(row):
13            for c in range(col):
14                headr,headc=r,c
15                tailr,tailc=row-1-r,col-1-c
16                preprod*=grid[headr][headc] % mod
17                sufprod*=grid[tailr][tailc] % mod
18                prefixprod[r][c]=preprod
19                suffixprod[row-1-r][col-1-c]=sufprod
20        for r in range(row):
21            for c in range(col):
22                pr,pc=-1,-1
23                if c-1<0:
24                    pr=r-1
25                    pc=col-1
26                else:
27                    pr=r
28                    pc=c-1
29                pp=1
30                if 0<=pr<row and 0<=pc<col:
31                    pp=prefixprod[pr][pc]
32                nr,nc=-1,-1
33                if c+1>col-1:
34                    nr=r+1
35                    nc=0
36                else:
37                    nr=r
38                    nc=c+1
39                sp=1
40                if 0<=nr<row and 0<=nc<col:
41                    sp=suffixprod[nr][nc]
42                res[r][c]=(pp*sp)%mod
43        return res
44                
45
46        
47        