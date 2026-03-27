# Last updated: 3/27/2026, 10:13:51 AM
1class Solution:
2    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
3        row=len(mat)
4        col=len(mat[0])
5        grid=copy.deepcopy(mat)
6        def shiftleft(grid,row):
7           f=grid[row].pop(0)
8           grid[row].append(f)
9        def shiftright(grid,row):
10            l=grid[row].pop()
11            grid[row].insert(0,l)
12        for _ in range(k):
13            for r in range(row):
14                if r%2==0:
15                    shiftleft(grid,r)
16                else:
17                    shiftright(grid,r)
18        return grid==mat
19
20
21
22