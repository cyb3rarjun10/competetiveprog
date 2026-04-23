# Last updated: 4/23/2026, 11:24:32 AM
1class UnionFind:
2    def __init__(self, n):
3        self.fa = list(range(n))
4        self.rank = [0] * n
5
6    def find(self, x):
7        if self.fa[x] != x:
8            self.fa[x] = self.find(self.fa[x])
9        return self.fa[x]
10
11    def union(self, x, y):
12        x = self.find(x)
13        y = self.find(y)
14        if x == y:
15            return
16        if self.rank[x] < self.rank[y]:
17            x, y = y, x
18        self.fa[y] = x
19        if self.rank[x] == self.rank[y]:
20            self.rank[x] += 1
21
22
23class Solution:
24    def minimumHammingDistance(
25        self,
26        source: List[int],
27        target: List[int],
28        allowedSwaps: List[List[int]],
29    ) -> int:
30        n = len(source)
31        uf = UnionFind(n)
32        for a, b in allowedSwaps:
33            uf.union(a, b)
34
35        sets = defaultdict(lambda: defaultdict(int))
36        for i in range(n):
37            f = uf.find(i)
38            sets[f][source[i]] += 1
39
40        ans = 0
41        for i in range(n):
42            f = uf.find(i)
43            if sets[f][target[i]] > 0:
44                sets[f][target[i]] -= 1
45            else:
46                ans += 1
47        return ans