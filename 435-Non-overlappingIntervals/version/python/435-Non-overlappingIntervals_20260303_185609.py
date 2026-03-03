# Last updated: 3/3/2026, 6:56:09 PM
1class Solution:
2    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
3        intervals.sort(key=lambda x:x[1])
4        res=0
5        prevend=-5 * (10**4)
6        for x,y in intervals:
7            if x<prevend:
8                res+=1
9                continue
10            prevend=y
11        return res
12
13
14            
15
16