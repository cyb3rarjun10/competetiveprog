# Last updated: 3/2/2026, 7:10:46 PM
1class Solution:
2    def minCostConnectPoints(self, points: List[List[int]]) -> int:
3        n = len(points)
4        
5        # BUG 2 FIX: Use indices 0 to n-1 as the node IDs
6        parent = [i for i in range(n)]
7        
8        def find(x):
9            if parent[x] != x:
10                parent[x] = find(parent[x])
11            return parent[x]
12            
13        def union(x, y):
14            root1 = find(x)
15            root2 = find(y)
16            if root1 == root2:
17                return False
18            parent[root1] = root2
19            return True
20            
21        edges = []
22        
23        # BUG 3 FIX: j starts at i+1 to avoid duplicate/reverse edges
24        for i in range(n):
25            for j in range(i + 1, n):
26                cost = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
27                edges.append((cost, i, j)) # Just store the cost and the two indices!
28                
29        # BUG 1 FIX: Kruskal's MUST sort the edges by weight first!
30        edges.sort()
31        
32        totcost = 0
33        edgecovered = 0
34        
35        # Now we unpack cost, and the two indices (u and v)
36        for cost, u, v in edges:
37            if union(u, v):
38                totcost += cost
39                edgecovered += 1
40                
41                # A tree with n nodes has exactly n-1 edges
42                if edgecovered == n - 1:
43                    break
44                    
45        return totcost