# Last updated: 5/6/2026, 1:46:26 PM
1# class Solution:
2#     def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
3#         row=len(boxGrid)
4#         col=len(boxGrid[0])
5#         for r in range(row):
6#             for c in range(col-1,-1,-1):
7#                 if boxGrid[r][c]=='#':
8#                     boxGrid[r][c]='.'
9#                     cc=c
10#                     while cc<col and boxGrid[r][cc]!='*' and boxGrid[r][cc]!='#':
11#                         cc+=1
12#                     cc-=1
13#                     boxGrid[r][cc]='#'
14#         transposed = [[boxGrid[j][i] for j in range(row)] for i in range(col)]
15#         print(boxGrid)                    
16
17class Solution:
18    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
19        m = len(box)
20        n = len(box[0])
21        result = [["" for _ in range(m)] for _ in range(n)]
22
23        # Create the transpose of the input grid in `result`
24        for i in range(n):
25            for j in range(m):
26                result[i][j] = box[j][i]
27
28        # Reverse each row in the transpose grid to complete the 90° rotation
29        for i in range(n):
30            result[i].reverse()
31
32        # Apply gravity to let stones fall to the lowest possible empty cell in each column
33        for j in range(m):
34            lowest_row_with_empty_cell = n - 1
35            # Process each cell in column `j` from bottom to top
36            for i in range(n - 1, -1, -1):
37                # Found a stone - let it fall to the lowest empty cell
38                if result[i][j] == "#":
39                    result[i][j] = "."
40                    result[lowest_row_with_empty_cell][j] = "#"
41                    lowest_row_with_empty_cell -= 1
42                # Found an obstacle - reset `lowest_row_with_empty_cell` to the row directly above it
43                if result[i][j] == "*":
44                    lowest_row_with_empty_cell = i - 1
45
46        return result
47                    
48            