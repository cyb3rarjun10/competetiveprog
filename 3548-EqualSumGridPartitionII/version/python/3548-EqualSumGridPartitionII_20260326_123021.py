# Last updated: 3/26/2026, 12:30:21 PM
1class Solution:
2    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
3        def rotate_90_clockwise(matrix):
4            return [list(row)[::-1] for row in zip(*matrix)]
5            
6        totalsum = 0
7        row = len(grid)
8        col = len(grid[0])
9        for r in range(row):
10            for c in range(col):
11                totalsum += grid[r][c]
12                
13        target = totalsum / 2
14        
15        for _ in range(4):
16            grid = rotate_90_clockwise(grid)
17            row = len(grid)
18            col = len(grid[0])
19            s = set()
20            res = 0
21            for r in range(row - 1):
22                for c in range(col):
23                    res += grid[r][c]
24                    s.add(grid[r][c] / 2)
25                if res == target:
26                    return True
27                diff = res - target
28                if diff > 0:
29                    if r==0 and col==1:
30                        continue
31                    elif r == 0 and col > 1:
32                        if diff == grid[0][0] / 2 or diff == grid[0][col - 1] / 2:
33                            return True
34                    elif r > 0 and col == 1:        
35                        if diff == grid[0][0] / 2 or diff == grid[r][0] / 2:
36                            return True
37                    else:
38                        if diff in s:
39                            return True      
40        return False
41        