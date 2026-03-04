# Last updated: 3/4/2026, 10:49:00 AM
1class Solution:
2    def numSpecial(self, mat: List[List[int]]) -> int:
3        r=len(mat)
4        c=len(mat[0])
5        res=0
6        for i in range(r):
7            for j in range(c):
8                if mat[i][j]==1:
9                    c1=0
10                    r1=0
11                    for row in range(r):
12                        if mat[row][j]==1:
13                            c1+=1
14                    for col in range(c):
15                        if mat[i][col]==1:
16                            r1+=1
17                    if r1==1 and c1==1:
18                        res+=1
19        return res