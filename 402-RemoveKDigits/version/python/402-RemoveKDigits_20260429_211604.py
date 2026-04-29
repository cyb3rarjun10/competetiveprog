# Last updated: 4/29/2026, 9:16:04 PM
1class Solution:
2    def removeKdigits(self, num: str, k: int) -> str:
3        stck=[]
4        for i in num:
5            while stck and stck[-1]>i and k>0:
6                k-=1
7                stck.pop()
8            stck.append(i)
9        while stck and k>0:
10            k-=1
11            stck.pop()
12        if not stck:
13            return "0"
14        temp="".join(stck).lstrip("0")
15        if temp=="":
16            return "0"
17        return temp
18