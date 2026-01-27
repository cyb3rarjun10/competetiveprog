# Last updated: 1/27/2026, 11:27:57 PM
1class Solution:
2    def minCost(self, n: int, edges: List[List[int]]) -> int:
3        adj=defaultdict(list)
4        for u,v,w in edges:
5            adj[u].append((v,w))
6            adj[v].append((u,2*w))
7        dist={i:float('inf') for i in range(n)}
8        dist[0]=0
9        pq=[(0,0)]
10        while pq:
11            currdist,currnode=heapq.heappop(pq)
12            if currdist>dist[currnode]:
13                continue
14            for nei,wei in adj[currnode]:
15                distance=currdist+wei
16                if distance<dist[nei]:
17                    dist[nei]=distance
18                    heapq.heappush(pq,(distance,nei))
19        return -1 if dist[n-1]==float('inf') else dist[n-1]