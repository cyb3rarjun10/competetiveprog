# Last updated: 3/11/2026, 8:53:24 AM
1class Solution:
2    def bitwiseComplement(self, n: int) -> int:
3        b=str(bin(n))
4        comp=""
5        for i in b[2:]:
6            if i=="1":
7                comp+="0"
8            else:
9                comp+="1"
10        return int(comp,2)