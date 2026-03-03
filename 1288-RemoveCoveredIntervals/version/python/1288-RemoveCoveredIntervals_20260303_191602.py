# Last updated: 3/3/2026, 7:16:02 PM
1class Solution:
2    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
3        intervals.sort(key=lambda x:(x[0],-x[1]))
4        end=0
5        remove=0
6        for x,y in intervals:
7            if y<=end:
8                remove+=1
9                continue
10            end=y
11        return len(intervals)-remove
12