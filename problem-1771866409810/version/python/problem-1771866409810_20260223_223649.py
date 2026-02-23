# Last updated: 2/23/2026, 10:36:49 PM
1class Solution:
2    def hasAllCodes(self, s: str, k: int) -> bool:
3        n=2**k
4        flag=[False]*n
5        for r in range(k-1,len(s)):
6            l=s[r-(k-1):r+1]
7            if int(l,2)<=n:
8                flag[int(l,2)]=True
9        if any(i==False for i in flag):
10            return False
11        return True