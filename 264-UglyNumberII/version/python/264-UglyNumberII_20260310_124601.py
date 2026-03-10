# Last updated: 3/10/2026, 12:46:01 PM
1class Solution:
2    def nthUglyNumber(self, n: int) -> int:
3        heap=[1]
4        s={1}
5        for i in range(n):
6            ugly=heapq.heappop(heap)
7            for f in [1,2,3,5]:
8                prod=ugly*f
9                if prod not in s:
10                    heapq.heappush(heap,prod)
11                    s.add(prod)
12        return ugly
13            
14        
15