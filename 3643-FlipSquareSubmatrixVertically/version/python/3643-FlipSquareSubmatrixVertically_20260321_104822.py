# Last updated: 3/21/2026, 10:48:22 AM
1class Solution:
2    def reverseSubmatrix(self, grid: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:
3        rows=len(grid)
4        cols=len(grid[0])
5        if x<0 or y<0 or x+k > rows or y+k > cols:
6            return grid
7        lowrow=x
8        lowcol=y
9        highrow=x+k -1
10        highcol=y+k -1
11        while lowrow<highrow:
12            for i in range(lowcol,highcol+1):
13                grid[lowrow][i],grid[highrow][i]=grid[highrow][i],grid[lowrow][i]
14            lowrow+=1
15            highrow-=1
16        return grid
17                
18        