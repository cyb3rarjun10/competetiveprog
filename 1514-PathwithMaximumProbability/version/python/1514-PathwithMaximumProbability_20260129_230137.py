# Last updated: 1/29/2026, 11:01:37 PM
1class Solution:
2    def maxProbability(self, n: int, edges: List[List[int]],
3                       succProb: List[float],
4                       start_node: int, end_node: int) -> float:
5
6        adj = defaultdict(list)
7        for (u, v), w in zip(edges, succProb):
8            adj[u].append((v, w))
9            adj[v].append((u, w))
10
11        pq = [(-1.0, start_node)]  # (-probability, node)
12        visited = set()
13
14        while pq:
15            neg_p, node = heapq.heappop(pq)
16            p = -neg_p
17
18            if node == end_node:
19                return p
20
21            if node in visited:
22                continue
23            visited.add(node)
24
25            for nei, w in adj[node]:
26                if nei not in visited:
27                    heapq.heappush(pq, (-(p * w), nei))
28
29        return 0.0
30
31