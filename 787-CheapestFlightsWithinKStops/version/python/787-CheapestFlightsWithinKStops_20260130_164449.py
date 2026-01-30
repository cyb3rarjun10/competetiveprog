# Last updated: 1/30/2026, 4:44:49 PM
1class Solution:
2    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
3        adj = defaultdict(list)
4        for u, v, w in flights:
5            adj[u].append((v, w))
6
7        dist = [[float('inf')] * (k + 2) for _ in range(n)]
8        dist[src][0] = 0
9
10        pq = [(0, src, 0)]  # cost, node, stops
11
12        while pq:
13            cost, node, stops = heapq.heappop(pq)
14
15            if node == dst:
16                return cost
17
18            if stops == k + 1:
19                continue
20
21            for nei, price in adj[node]:
22                new_cost = cost + price
23                if new_cost < dist[nei][stops + 1]:
24                    dist[nei][stops + 1] = new_cost
25                    heapq.heappush(pq, (new_cost, nei, stops + 1))
26
27        return -1