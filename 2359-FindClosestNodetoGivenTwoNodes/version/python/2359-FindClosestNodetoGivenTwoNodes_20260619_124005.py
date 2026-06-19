# Last updated: 6/19/2026, 12:40:05 PM
1class Solution:
2    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
3        n=len(edges)
4        node1toall=[-1]*n
5        node2toall=[-1]*n
6
7        def getdist(node,dist):
8            curr=node
9            step=0
10            while curr!=-1  and dist[curr]==-1: #not dead end , not visited already(loop)
11                dist[curr]=step
12                step+=1
13                curr=edges[curr]
14            
15
16        getdist(node1,node1toall)
17        getdist(node2,node2toall)
18        res=-1
19        mindist=float('inf')
20        for i in range(n):
21            if node1toall[i]!=-1 and node2toall[i]!=-1:
22                dist=max(node1toall[i],node2toall[i])
23                if dist<mindist:
24                    mindist=dist
25                    res=i
26        return res
27                