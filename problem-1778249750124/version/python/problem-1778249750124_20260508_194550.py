# Last updated: 5/8/2026, 7:45:50 PM
1MX = 1_000_001
2factors = [[] for _ in range(MX)]
3for i in range(2, MX):
4    if not factors[i]:
5        for j in range(i, MX, i):
6            factors[j].append(i)
7
8
9class Solution:
10    def minJumps(self, nums: List[int]) -> int:
11        n = len(nums)
12        edges = defaultdict(list)
13        for i, a in enumerate(nums):
14            for p in factors[a]:
15                edges[p].append(i)
16        res = 0
17        seen = [False] * n
18        seen[0] = True
19        q = [0]
20        while True:
21            q2 = []
22            for i in q:
23                if i == n - 1:
24                    return res
25                if i > 0 and not seen[i - 1]:
26                    seen[i - 1] = True
27                    q2.append(i - 1)
28                if i < n - 1 and not seen[i + 1]:
29                    seen[i + 1] = True
30                    q2.append(i + 1)
31                if len(factors[nums[i]]) == 1:
32                    p = nums[i]
33                    for j in edges[p]:
34                        if not seen[j]:
35                            seen[j] = True
36                            q2.append(j)
37                    edges[p].clear()
38            q = q2
39            res += 1