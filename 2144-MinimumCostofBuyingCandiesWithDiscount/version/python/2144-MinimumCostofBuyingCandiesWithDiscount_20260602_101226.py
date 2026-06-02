# Last updated: 6/2/2026, 10:12:26 AM
1class Solution:
2    def minimumCost(self, cost: List[int]) -> int:
3        cost.sort()
4        if len(cost)<3:
5            return sum(cost)
6        n=len(cost)
7        tot=0
8        for i in range(n-1,-1,-3):
9            tot+=cost[i]
10            if i-1>=0:
11                tot+=cost[i-1]
12        return tot