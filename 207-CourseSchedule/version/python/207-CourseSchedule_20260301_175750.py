# Last updated: 3/1/2026, 5:57:50 PM
1class Solution:
2    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
3        n=numCourses
4        #kahn algo (topo sort)
5        indegree=[0]*n
6        adj=defaultdict(list)
7        for v,u in prerequisites:
8            adj[u].append(v)
9        for i in adj:
10            for node in adj[i]:
11                indegree[node]+=1
12        queue=deque()
13        for i in range(n):
14            if indegree[i]==0:
15                queue.append(i)
16        coursecompleted=0
17        while queue:
18            curr=queue.popleft()
19            coursecompleted+=1
20            for nei in adj[curr]:
21                indegree[nei]-=1
22                if indegree[nei]==0:
23                    queue.append(nei)
24        return coursecompleted==numCourses
25            
26