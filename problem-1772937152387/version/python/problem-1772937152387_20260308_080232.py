# Last updated: 3/8/2026, 8:02:32 AM
1class Solution:
2    def minimumIndex(self, capacity: list[int], itemSize: int) -> int:
3        minsize=float('inf')
4        minidx=-1
5        for i in range(len(capacity)):
6            if capacity[i]>=itemSize:
7                if capacity[i]<minsize:
8                    minsize=capacity[i]
9                    minidx=i
10        return minidx