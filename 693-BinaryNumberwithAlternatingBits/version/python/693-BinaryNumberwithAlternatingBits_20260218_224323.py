# Last updated: 2/18/2026, 10:43:23 PM
1class Solution:
2    def hasAlternatingBits(self, n: int) -> bool:
3        b=str(bin(n))
4        for i in range(len(b)-1):
5            if b[i]==b[i+1]:
6                return False
7        return True