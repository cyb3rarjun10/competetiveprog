# Last updated: 3/17/2026, 7:14:42 PM
1class Solution:
2    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
3        def largestrec(heights):
4            n=len(heights)
5            stck=[]
6            re=[-1]*n
7            le=[-1]*n
8            for h in range(n-1,-1,-1):
9                while stck and heights[h]<=heights[stck[-1]]:
10                    stck.pop()
11                if not stck:
12                    re[h]=n-1
13                else:
14                    re[h]=stck[-1]-1
15                stck.append(h)
16            stck=[]
17            for h in range(n):
18                while stck and heights[h]<=heights[stck[-1]]:
19                    stck.pop()
20                if not stck:
21                    le[h]=0
22                else:
23                    le[h]=stck[-1]+1
24                stck.append(h)
25            maxrec=float('-inf')
26            for curr in range(len(heights)):
27                rec=((re[curr]-le[curr]) +1)*heights[curr]
28                maxrec=max(maxrec,rec)
29            return maxrec
30        res=0
31        row=len(matrix)
32        col=len(matrix[0])
33        for r in range(row):
34            for c in range(col):
35                if r>0:
36                    if matrix[r][c]!=0:
37                        if matrix[r-1][c]!=0:
38                            matrix[r][c]=matrix[r-1][c]+1
39            maxasofnow=largestrec(sorted(matrix[r],reverse=True))
40            res=max(res,maxasofnow)
41        return res