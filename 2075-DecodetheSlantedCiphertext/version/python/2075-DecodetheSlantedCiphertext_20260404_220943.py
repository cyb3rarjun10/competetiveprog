# Last updated: 4/4/2026, 10:09:43 PM
1class Solution:
2    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
3        l=len(encodedText)
4        cols=l//rows
5        mat=[["" for i in range(cols)]for j in range(rows)]
6        idx=0
7        for i in range(rows):
8            for j in range(cols):
9                mat[i][j]=encodedText[idx]
10                idx+=1
11        res=""
12        for cstart in range(cols):
13            i=0
14            j=cstart
15            while i<rows and j<cols:
16                res+=mat[i][j]
17                i+=1
18                j+=1
19        return res.rstrip()
20