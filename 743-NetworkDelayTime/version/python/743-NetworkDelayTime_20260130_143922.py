# Last updated: 1/30/2026, 2:39:22 PM
1class Solution:
2    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
3        adj=defaultdict(list)
4        for u,v,w in times:
5            adj[u].append((v,w))
6        dist={node:float('inf') for node in range(1,n+1)}
7        dist[k]=0
8        pq=[(k,0)] #(node,timetaken)
9        while pq:
10            currnode,currtime=heapq.heappop(pq)
11            if currtime>dist[currnode]:
12                continue
13            for nei,time in adj[currnode]:
14                tot=currtime+time
15                if tot<dist[nei]:
16                    dist[nei]=tot
17                    heapq.heappush(pq,(nei,tot))
18        maxtime=float('-inf')
19        for i in range(1,n+1):
20            maxtime=max(maxtime,dist[i])
21        return maxtime if maxtime!=float('inf') else -1