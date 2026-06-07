# Last updated: 6/7/2026, 8:15:09 AM
1class Solution:
2    def generateValidStrings(self, n: int, k: int) -> list[str]:
3        res=[]
4        def recurse(idx,cost,prev,path):
5            if idx==n:
6                res.append("".join(path))
7                return
8                
9            path.append('0')
10            recurse(idx+1,cost,'0',path)
11            path.pop()
12
13            if idx+cost<=k and prev!='1':
14                path.append('1')
15                recurse(idx+1,cost+idx,'1',path)
16                path.pop()
17        recurse(0,0,'0',[])
18        return res
19            
20            