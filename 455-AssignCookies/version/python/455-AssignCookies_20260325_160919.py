# Last updated: 3/25/2026, 4:09:19 PM
1class Solution:
2    def findContentChildren(self, g: List[int], s: List[int]) -> int:
3        g.sort()
4        s.sort()
5        output=0
6        j=0
7        for i in range(len(s)):
8            if g[j]<=s[i]:
9                j+=1
10                output+=1
11            if j==len(g):
12                break
13        return output
14