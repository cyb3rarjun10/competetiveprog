# Last updated: 3/11/2026, 12:17:51 AM
1class Solution:
2    def partition(self, s: str) -> List[List[str]]:
3        n=len(s)
4        res=[]
5        def recurse(idx,path):
6            if idx==n:
7                res.append(path)
8                return
9            for i in range(idx+1,n+1):
10                curr=s[idx:i]
11                if curr==curr[::-1]:
12                    recurse(i,path+[curr])
13        recurse(0,[])
14        return res