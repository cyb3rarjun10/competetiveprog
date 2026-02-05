# Last updated: 2/5/2026, 8:44:21 PM
1class Solution:
2    def numTilePossibilities(self, tiles: str) -> int:
3        d=Counter(tiles)
4        count=0
5        def dfs(s,d):
6            nonlocal count
7            for i in d.keys():
8                if d[i]>0:
9                    d[i]-=1
10                    count+=1
11                    dfs(s+i,d)
12                    d[i]+=1
13        dfs("",d)
14        return count
15        
16            
17            
18            