# Last updated: 1/29/2026, 6:58:43 PM
1class Solution:
2    def minimumCost(self, source: str, target: str,
3                    original: List[str], changed: List[str], cost: List[int]) -> int:
4
5        INF = float('inf')
6        dist = [[INF]*26 for _ in range(26)]
7
8        # distance to self = 0
9        for i in range(26):
10            dist[i][i] = 0
11
12        # direct transformations
13        for o, c, w in zip(original, changed, cost):
14            u = ord(o) - ord('a')
15            v = ord(c) - ord('a')
16            dist[u][v] = min(dist[u][v], w)   # important if multiple edges
17
18        # Floyd–Warshall
19        for k in range(26):
20            for i in range(26):
21                for j in range(26):
22                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
23
24        # compute answer
25        ans = 0
26        for s, t in zip(source, target):
27            u = ord(s) - ord('a')
28            v = ord(t) - ord('a')
29            if dist[u][v] == INF:
30                return -1
31            ans += dist[u][v]
32
33        return ans
34