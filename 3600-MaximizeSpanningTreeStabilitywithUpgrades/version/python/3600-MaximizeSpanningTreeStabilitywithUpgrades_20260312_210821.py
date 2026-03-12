# Last updated: 3/12/2026, 9:08:21 PM
1class DSU:
2    def __init__(self, n):
3        self.parent = list(range(n))
4        self.components = n
5
6    def find(self, x):
7        if self.parent[x] != x:
8            self.parent[x] = self.find(self.parent[x])
9        return self.parent[x]
10
11    def unite(self, a, b):
12        pa = self.find(a)
13        pb = self.find(b)
14
15        if pa == pb:
16            return False
17
18        self.parent[pb] = pa
19
20        self.components -= 1
21        return True
22
23
24class Solution:
25    def canAchieve(self, n, edges, k, x):
26        dsu = DSU(n)
27
28        # Mandatory edges
29        for u, v, s, must in edges:
30            if must == 1:
31                if s < x:
32                    return False
33                if not dsu.unite(u, v):
34                    return False
35
36        # Free optional edges
37        for u, v, s, must in edges:
38            if must == 0 and s >= x:
39                dsu.unite(u, v)
40
41        # Upgrade edges
42        used_upgrades = 0
43
44        for u, v, s, must in edges:
45            if must == 0 and s < x and 2 * s >= x:
46                if dsu.unite(u, v):
47                    used_upgrades += 1
48                    if used_upgrades > k:
49                        return False
50
51        return dsu.components == 1
52
53    def maxStability(self, n, edges, k):
54        # Check mandatory edges cycle
55        dsu = DSU(n)
56        for u, v, s, must in edges:
57            if must == 1:
58                if not dsu.unite(u, v):
59                    return -1
60
61        low, high = 1, 200000
62        ans = -1
63
64        while low <= high:
65            mid = (low + high) // 2
66
67            if self.canAchieve(n, edges, k, mid):
68                ans = mid
69                low = mid + 1
70            else:
71                high = mid - 1
72
73        return ans