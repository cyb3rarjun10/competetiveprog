# Last updated: 2/5/2026, 6:25:55 PM
1class Solution:
2    def validStrings(self, n: int) -> List[str]:
3        res=[]
4        def dfs(s):
5            if len(s)==n:
6                res.append(s)
7                return
8            if s[-1]=="0":
9                dfs(s+"1")
10            else:
11                dfs(s+"0")
12                dfs(s+"1")
13        dfs("0")
14        dfs("1")
15        return res
16        
17