# Last updated: 2/6/2026, 9:54:51 PM
1class Solution:
2    def partition(self, s: str) -> List[List[str]]:
3        def checkpal(s):
4            return s==s[::-1]
5        res=[]
6        def recurse(curr,s):
7            if s=="":
8                res.append(curr)
9            for i in range(len(s)):
10                if checkpal(s[:i+1]):
11                    recurse(curr+[s[:i+1]], s[i+1:])
12        recurse([],s)
13        return res