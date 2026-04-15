# Last updated: 4/15/2026, 5:23:16 PM
1class Solution:
2    def equalPairs(self, grid: List[List[int]]) -> int:
3        row,col=len(grid),len(grid)
4        d=defaultdict(int)
5        for i in range(row):
6            temp=""
7            for j in range(col):
8                temp+=str(grid[i][j])
9                temp+="."
10            d[temp]+=1
11        e=defaultdict(int)
12        for j in range(col):
13            temp=""
14            for i in range(row):
15                temp+=str(grid[i][j])
16                temp+="."
17            e[temp]+=1
18        res=0
19        for key in d:
20            if key in e:
21                res+=d[key]*e[key]
22        return res
23