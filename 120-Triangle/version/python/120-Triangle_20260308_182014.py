# Last updated: 3/8/2026, 6:20:14 PM
1class Solution:
2    def minimumTotal(self, triangle: List[List[int]]) -> int:
3        n=len(triangle)
4        @cache
5        def recurse(row,col):
6            if row==n-1:
7                return triangle[row][col]
8            move1=recurse(row+1,col)+triangle[row][col]
9            move2=recurse(row+1,col+1)+triangle[row][col]
10            return min(move1,move2)
11        return recurse(0,0)
12        
13