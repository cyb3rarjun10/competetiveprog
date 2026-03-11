# Last updated: 3/11/2026, 11:16:19 AM
1class Solution:
2    def gameOfLife(self, board: List[List[int]]) -> None:
3        """
4        Do not return anything, modify board in-place instead.
5        """
6        d={}
7        row=len(board)
8        col=len(board[0])
9        directions=[(-1,0),(1,0),(0,-1),(0,1),(-1,-1),(1,-1),(-1,1),(1,1)]
10        for r in range(row):
11            for c in range(col):
12                ones=0
13                for nr,nc in directions:
14                    cr,cc=r+nr,c+nc
15                    if 0<=cr<row and 0<=cc<col:
16                        if board[cr][cc]==1:
17                            ones+=1
18                if board[r][c]==1:
19                    if ones<2:
20                        d[(r,c)]=0
21                    if ones>3:
22                        d[(r,c)]=0
23                elif board[r][c]==0:
24                    if ones==3:
25                        d[(r,c)]=1
26        for r,c in d:
27            board[r][c]=d[(r,c)]