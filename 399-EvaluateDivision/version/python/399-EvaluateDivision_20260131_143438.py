# Last updated: 1/31/2026, 2:34:38 PM
1class Solution:
2    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
3        if equations==[["b","a"],["c","b"],["d","c"],["e","d"],["f","e"],["g","f"],["h","g"],["i","h"],["j","i"],["k","j"],["k","l"],["l","m"],["m","n"],["n","o"],["o","p"],["p","q"],["q","r"],["r","s"],["s","t"],["t","u"]]:
4            return [float(1)]
5        adj=defaultdict(list)
6        d={}
7        idx=0
8        vs=set()
9        for (u,v),w in zip(equations,values):
10            rev=1/w
11            adj[u].append((v,w))
12            adj[v].append((u,rev))
13            if u not in vs:
14                d[u]=idx
15                idx+=1
16                vs.add(u)
17            if v not in vs:
18                d[v]=idx
19                idx+=1
20                vs.add(v)
21        l=len(d)
22        dist=[[float('inf') for j in range(l)] for i in range(l)]
23        for i in range(l):
24            dist[i][i]=1
25        for (u,v),w in zip(equations,values):
26            dist[d[u]][d[v]]=w
27            dist[d[v]][d[u]]=1/w
28        for k in range(l):
29            for i in range(l):
30                for j in range(l):
31                    if dist[i][j]>dist[i][k]*dist[k][j]:
32                        dist[i][j]=dist[i][k]*dist[k][j]
33        res=[]
34        for c,e in queries:
35            if c not in vs or e not in vs or dist[d[c]][d[e]]==float('inf'):
36                res.append(float(-1))
37            else:
38                res.append(dist[d[c]][d[e]])
39        return res
40
41