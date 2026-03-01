# Last updated: 3/1/2026, 9:08:57 PM
1class Solution:
2    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
3        n=len(edges)
4        parent=[i for i in range(n+1)]
5        def find(x):
6            if parent[x]!=x:
7                parent[x]=find(parent[x])
8            return parent[x]
9        def union(u,v):
10            root1=find(u)
11            root2=find(v)
12            if root1==root2:
13                return False
14            parent[root1]=root2
15            return True
16        for u,v in edges:
17            if not union(u,v):
18                return [u,v]
19        
20
21            