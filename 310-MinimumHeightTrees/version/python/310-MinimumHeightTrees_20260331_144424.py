# Last updated: 3/31/2026, 2:44:24 PM
1class Solution:
2    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
3        # Edge case: If there are 2 or fewer nodes, they can all be roots
4        if n <= 2:
5            return [i for i in range(n)]
6
7        # 1. Build the adjacency list and an array to track degrees
8        adj = defaultdict(set)
9        for u, v in edges:
10            adj[u].add(v)
11            adj[v].add(u)
12
13        # 2. Find the first layer of leaves (degree == 1)
14        leaves = deque()
15        for i in range(n):
16            if len(adj[i]) == 1:
17                leaves.append(i)
18
19        # 3. Peel the onion! 
20        remaining_nodes = n
21        
22        # We stop when there are 1 or 2 nodes left (the centroids)
23        while remaining_nodes > 2:
24            # We are removing a whole layer of leaves
25            leaves_count = len(leaves)
26            remaining_nodes -= leaves_count
27            
28            for _ in range(leaves_count):
29                leaf = leaves.popleft()
30                
31                # The leaf only has one neighbor. Get it and remove the connection.
32                neighbor = adj[leaf].pop()
33                adj[neighbor].remove(leaf)
34                
35                # If removing that connection turned the neighbor into a new leaf, add it!
36                if len(adj[neighbor]) == 1:
37                    leaves.append(neighbor)
38
39        return list(leaves)