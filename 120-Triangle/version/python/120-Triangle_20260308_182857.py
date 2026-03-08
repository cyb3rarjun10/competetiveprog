# Last updated: 3/8/2026, 6:28:57 PM
1class Solution:
2    def minimumTotal(self, triangle: list[list[int]]) -> int:
3        n = len(triangle)
4        
5        # Start at the second-to-last row, and move UP to row 0
6        for row in range(n - 2, -1, -1):
7            
8            # Loop through every cell in the current row
9            for col in range(len(triangle[row])):
10                
11                # The best path is our current cell + the MIN of the two cells directly below us
12                best_future = min(triangle[row + 1][col], triangle[row + 1][col + 1])
13                
14                # Overwrite the current cell!
15                triangle[row][col] += best_future
16                
17        # The top tip of the pyramid now contains the absolute best path sum
18        return triangle[0][0]
19        
20