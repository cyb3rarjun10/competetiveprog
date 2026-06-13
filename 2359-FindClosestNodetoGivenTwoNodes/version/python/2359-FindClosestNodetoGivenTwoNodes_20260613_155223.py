# Last updated: 6/13/2026, 3:52:23 PM
1class Solution:
2    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
3        node1toall={}
4        node2toall={}
5        def bfs(node,dict):
6            queue=deque([node])
7            v=set()
8            v.add(node)
9            level=0
10            while queue:
11                l=len(queue)
12                for _ in range(l):
13                    curr=queue.popleft()
14                    dict[curr]=level
15                    if edges[curr]!=-1 and edges[curr] not in v:
16                        queue.append(edges[curr])
17                        v.add(edges[curr])
18                level+=1
19        bfs(node1,node1toall)
20        bfs(node2,node2toall)
21        res=-1
22        mindist=float('inf')
23        for i in range(len(edges)):
24            if i in node1toall and i in node2toall:
25                dist=max(node1toall[i],node2toall[i])
26                if dist<mindist:
27                    mindist=dist
28                    res=i
29        return res
30                