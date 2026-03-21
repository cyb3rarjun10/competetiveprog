# Last updated: 3/21/2026, 4:40:58 PM
1class Solution:
2    def getMaximumGold(self, grid: List[List[int]]) -> int:
3        row=len(grid)
4        col=len(grid[0])
5        elts=row*col
6        directions=[(0,-1),(0,1),(1,0),(-1,0)]
7        # def recurse(cr,cc,count):
8        #     if count==elts:
9        #         return 0
10        #     temp=[]
11        #     for dr,dc in directions:
12        #         nr,nc=cr+dr,cc+dc
13        #         if 0<=nr<row and 0<=nc<0 and grid[nr][nc]!=0:
14        #             goldcollected=grid[cr][cc]+recurse(nr,nc,count+1)
15        #             temp.append(goldcollected)
16        #     return min(temp) if temp else 0
17        # res=0
18        # for i in range(row):
19        #     for j in range(col):
20        #         x=recurse(i,j,0)
21        #         res=max(res,x)
22        # return res
23
24# 1. Put the starting footprint inside the tuple!
25        stck = []
26        for i in range(row):
27            for j in range(col):
28                if grid[i][j] != 0:
29                    # Tuple: (row, col, current_gold, visited_set)
30                    stck.append((i, j, grid[i][j], {(i, j)}))
31                    
32        res = 0
33
34        while stck:
35            # 2. Unpack the historical memory for THIS specific path
36            cr, cc, curr, v = stck.pop()
37            res = max(res, curr)
38            
39            for dr, dc in directions:
40                nr, nc = cr + dr, dc + cc
41                
42                # 3. Check against this path's historical memory
43                if 0 <= nr < row and 0 <= nc < col and grid[nr][nc] != 0 and (nr, nc) not in v:
44                    
45                    # 4. Create a copy of the memory for the next step so branches don't share
46                    new_v = v.copy()
47                    new_v.add((nr, nc))
48                    
49                    # 5. Pack the new memory into the backpack for the next step
50                    stck.append((nr, nc, curr + grid[nr][nc], new_v))
51                    
52        return res
53
54
55