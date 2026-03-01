# Last updated: 3/1/2026, 3:35:46 PM
1class Solution:
2    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
3        dist=[float('inf')]*(n+1)
4        dist[src]=0
5        for _ in range(k+1):
6            temp=dist.copy()
7            for u,v,w in flights:
8                if dist[u]!=float('inf') and  dist[u]+w < temp[v]:
9                    temp[v]=dist[u]+w
10            dist=temp
11        return dist[dst] if dist[dst] !=float('inf') else -1
12
13