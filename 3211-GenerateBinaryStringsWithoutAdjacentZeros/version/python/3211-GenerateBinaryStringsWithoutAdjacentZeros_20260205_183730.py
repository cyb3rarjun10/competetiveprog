# Last updated: 2/5/2026, 6:37:30 PM
1class Solution:
2    def validStrings(self, n: int) -> List[str]:
3        res=[]
4        stck=["0","1"]
5        while stck:
6            curr=stck.pop()
7            if len(curr)==n:
8                res.append(curr)
9                continue
10            if curr[-1]=="0":
11                stck.append(curr+"1")
12            else:
13                stck.append(curr+"1")
14                stck.append(curr+"0")
15        return res
16            
17
18