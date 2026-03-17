# Last updated: 3/17/2026, 1:59:53 PM
1class Solution:
2    def largestRectangleArea(self, heights: List[int]) -> int:
3        n=len(heights)
4        #re=[0,5,3,3,5,5]
5        #le=[0,0,2,3,2,5]
6        stck=[]
7        re=[-1]*n
8        le=[-1]*n
9        for h in range(n-1,-1,-1):
10            while stck and heights[h]<=heights[stck[-1]]:
11                stck.pop()
12            if not stck:
13                re[h]=n-1
14            else:
15                re[h]=stck[-1]-1
16            stck.append(h)
17        stck=[]
18        for h in range(n):
19            while stck and heights[h]<=heights[stck[-1]]:
20                stck.pop()
21            if not stck:
22                le[h]=0
23            else:
24                le[h]=stck[-1]+1
25            stck.append(h)
26        print(re)
27        print(le)
28        maxrec=float('-inf')
29        for curr in range(len(heights)):
30            rec=((re[curr]-le[curr]) +1)*heights[curr]
31            maxrec=max(maxrec,rec)
32        return maxrec
33