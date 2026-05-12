# Last updated: 5/12/2026, 8:56:29 AM
1class Solution:
2    def minimumEffort(self, tasks: List[List[int]]) -> int:
3        tasks=sorted(tasks, key=lambda x:x[1]-x[0])
4        res=0
5        for need,min in tasks:
6            res=max(res+need,min)
7        return res