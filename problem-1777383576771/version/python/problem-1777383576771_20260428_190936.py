# Last updated: 4/28/2026, 7:09:36 PM
1class Solution:
2    def minOperations(self, grid: List[List[int]], x: int) -> int:
3        l=[]
4        for row in grid:
5            l+=row
6        l.sort()
7        n=len(l)
8        target=l[n//2]
9        k=target%x
10        cost=0
11        for i in range(n):
12            if l[i]%x != k:
13                return -1
14            cost+=(abs(target-l[i]))//x
15            print(l[i],cost)
16        return cost
17