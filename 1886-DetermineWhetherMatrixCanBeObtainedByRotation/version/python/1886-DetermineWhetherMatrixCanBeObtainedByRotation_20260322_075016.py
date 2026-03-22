# Last updated: 3/22/2026, 7:50:16 AM
1class Solution:
2    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
3        n=len(mat)
4        def isequal(mat,target):
5            for i in range(n):
6                for j in range(n):
7                    if mat[i][j]!=target[i][j]:
8                        return False
9            return True
10        def rotate(mat):
11            temp = [row[:] for row in mat]
12            for i in range(n):
13                for j in range(n):
14                    mat[j][n-i-1]=temp[i][j]
15        for _ in range(4):
16            rotate(mat)
17            if isequal(mat,target):
18                return True
19        return False
20