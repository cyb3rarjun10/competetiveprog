# Last updated: 1/12/2026, 4:54:58 PM
1class Solution:
2    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
3        res=0
4        n=len(points)
5        for i in range(1,n):
6            x1,y1=points[i-1][0],points[i-1][1]
7            x2,y2=points[i][0],points[i][1]
8            dx=abs(x2-x1)
9            dy=abs(y2-y1)
10            res+=max(dx,dy)
11        return res
12