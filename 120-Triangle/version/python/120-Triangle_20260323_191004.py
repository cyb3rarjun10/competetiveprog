# Last updated: 3/23/2026, 7:10:04 PM
1class Solution:
2    def minimumTotal(self, triangle: list[list[int]]) -> int:
3        n = len(triangle)
4        if n==1:
5            return triangle[0][0]
6        for r in range(n-2,-1,-1):
7            for c in range(r+1):
8                triangle[r][c]=triangle[r][c]+min(triangle[r+1][c],triangle[r+1][c+1])
9        return triangle[0][0]
10
11