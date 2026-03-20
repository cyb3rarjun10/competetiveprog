# Last updated: 3/20/2026, 8:51:21 PM
1class Solution:
2    def minAbsDiff(self, grid: List[List[int]], k: int) -> List[List[int]]:
3        r=len(grid)
4        c=len(grid[0])
5        res=[]
6        for i in range(r-k +1):
7            row=[]
8            for j in range(c-k +1):
9                values=[]
10                for x in range(i, i+k):
11                    for y in range(j, j+k):
12                        values.append(grid[x][y])
13                values=sorted(set(values))
14
15                if len(values)<=1:
16                    row.append(0)
17                else:
18                    diff=min(abs(values[w]-values[w+1])for w in range(len(values)-1))
19                    row.append(diff)
20            res.append(row)
21        return res
22                    