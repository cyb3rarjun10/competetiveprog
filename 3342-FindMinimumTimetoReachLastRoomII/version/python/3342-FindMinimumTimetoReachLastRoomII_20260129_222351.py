# Last updated: 1/29/2026, 10:23:51 PM
1class Solution:
2    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
3        row=len(moveTime)
4        col=len(moveTime[0])
5        dir=[(-1,0),(1,0),(0,-1),(0,1)]
6        v=set()
7        pq=[(0,0,0)] #(currtime,row,col)
8        while pq:
9            ct,cr,cc=heapq.heappop(pq)
10            if (cr,cc) in v:
11                continue
12            v.add((cr,cc))
13            if cr==row-1 and cc==col-1:
14                return ct
15            for dr,dc in dir:
16                nr,nc=cr+dr,cc+dc
17                if(nr+nc)%2==0:
18                    inc=2
19                else:
20                    inc=1
21                if 0<=nr<row and 0<=nc<col and (nr,nc) not in v:
22                    heapq.heappush(pq,(max(moveTime[nr][nc],ct)+inc,nr,nc))
23        return -1
24