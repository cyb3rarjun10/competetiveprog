# Last updated: 4/27/2026, 10:26:10 PM
1class Solution:
2    TRANS = [
3        [-1, 1, -1, 3],
4        [0, -1, 2, -1],
5        [3, 2, -1, -1],
6        [1, -1, -1, 2],
7        [-1, 0, 3, -1],
8        [-1, -1, 1, 0]
9    ]
10    DIRS = [[-1, 0], [0, 1], [1, 0], [0, -1]]
11    START = [[1, 3], [0, 2], [2, 3], [1, 2], [0, 3], [0, 1]]
12
13    def hasValidPath(self, grid: List[List[int]]) -> bool:       
14        m, n = len(grid), len(grid[0])
15        if m == 1 and n == 1: return True
16
17        def check(d):
18            if d == -1: return False
19            r, c = self.DIRS[d]
20            # O(1) Space
21            while 0 <= r < m and 0 <= c < n:               
22                d = self.TRANS[grid[r][c] - 1][d]
23                if d == -1: return False
24                if r == 0 and c == 0: return False
25                if r == m - 1 and c == n - 1: return True
26                
27                dr, dc = self.DIRS[d] 
28                r += dr
29                c += dc
30            return False
31
32        a, b = self.START[grid[0][0] - 1]
33        return check(a) or check(b)