# Last updated: 4/12/2026, 8:10:17 AM
1class Solution:
2    def findDegrees(self, matrix: list[list[int]]) -> list[int]:
3        return [sum(row) for row in matrix]