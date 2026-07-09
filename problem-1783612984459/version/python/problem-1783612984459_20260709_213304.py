# Last updated: 7/9/2026, 9:33:04 PM
1class Solution:
2    def findCircleNum(self, isConnected: List[List[int]]) -> int:
3        adj=defaultdict(list)
4        n=len(isConnected)
5        for r in range(n):
6            for c in range(n):
7                if isConnected[r][c]==1 and r+1 != c+1:
8                    adj[r+1].append(c+1)              
9        v=set()
10        def dfs(node):
11            stck=[node]
12            v.add(node)
13            while stck:
14                curr=stck.pop()
15                for nei in adj[curr]:
16                    if nei not in v:
17                        v.add(nei)
18                        stck.append(nei)
19
20        count=0
21        for i in range(1,n+1):
22            if i not in v:
23                count+=1
24                dfs(i)
25        return count
26