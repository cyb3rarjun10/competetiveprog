# Last updated: 3/16/2026, 1:45:12 PM
1class Solution:
2    def getBiggestThree(self, grid: List[List[int]]) -> List[int]:
3        m, n = len(grid), len(grid[0])
4        def helper(dx, dy, l, x, y):
5            summ=0
6            for i in range(l):
7                x+=dx
8                y+=dy
9                if not((0<=x<m) and (0<=y<n)):
10                    return -1,-1,-1
11                summ+=grid[x][y]
12            return x, y, summ
13        
14        res=set()
15        dir = [(1, 1), (1, -1), (-1, -1), (-1, 1)]
16        for i in range(m):
17            for j in range(n):
18                res.add(grid[i][j])
19                for le in range(min(m,n)//2):
20                    cx, cy = i, j
21                    s = 0
22                    #print(cx, cy, le)
23                    for dx, dy in dir:
24                        cx, cy, cs = helper(dx, dy, le + 1, cx, cy)
25                        #print(cx, cy)
26                        if cx == -1: break
27                        s += cs
28                    
29                    else:
30                        #print(s, i, j, le + 1)
31                        res.add(s)
32                    
33        
34        return sorted(list(res),reverse=True)[:3]
35
36                        
37
38