# Last updated: 4/20/2026, 4:41:32 PM
1class Solution:
2    def maxDistance(self, colors: List[int]) -> int:
3        maxdist=float('-inf')
4        for i in range(len(colors)):
5            for j in range(len(colors)-1,i,-1):
6                if colors[i]!=colors[j]:
7                    maxdist=max(maxdist,j-i)
8        return maxdist