# Last updated: 3/1/2026, 2:47:02 PM
1import heapq
2from collections import defaultdict
3from typing import List
4
5class Solution:
6    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
7        adj = defaultdict(list)
8        for u, v, w in times:
9            adj[u].append((v, w))
10            
11        dist = {node: float('inf') for node in range(1, n + 1)}
12        dist[k] = 0
13        
14        # FIX: (time_taken, node) so heapq sorts by time
15        pq = [(0, k)] 
16        
17        while pq:
18            currtime, currnode = heapq.heappop(pq)
19            
20            # Stale entry optimization
21            if currtime > dist[currnode]:
22                continue
23                
24            for nei, time in adj[currnode]:
25                tot = currtime + time
26                if tot < dist[nei]:
27                    dist[nei] = tot
28                    heapq.heappush(pq, (tot, nei)) # FIX: (time, node)
29                    
30        maxtime = max(dist.values())
31        return maxtime if maxtime != float('inf') else -1