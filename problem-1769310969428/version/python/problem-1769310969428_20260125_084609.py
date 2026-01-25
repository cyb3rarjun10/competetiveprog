# Last updated: 1/25/2026, 8:46:09 AM
1class Solution:
2    def specialNodes(self, n: int, edges: List[List[int]], x: int, y: int, z: int) -> int:
3        adj=defaultdict(list)
4        special=0
5        
6        for u,v in edges:
7            adj[u].append(v)
8            adj[v].append(u)
9            
10        def bfs(src):
11            dist =[-1] * n
12            queue = deque([src])
13            dist[src] = 0
14
15            while queue:
16                node = queue.popleft()
17                for nei in adj[node]:
18                    if dist[nei] == -1:
19                        dist[nei] = dist[node] + 1
20                        queue.append(nei)
21            return dist
22
23        xd=bfs(x)
24        yd=bfs(y)
25        zd=bfs(z)
26
27        for i in range(n):
28            temp=[xd[i],yd[i],zd[i]]
29            temp.sort()
30            a=temp[0]
31            b=temp[1]
32            c=temp[2]
33            if a*a + b*b == c*c:
34                special+=1
35        return special
36
37        