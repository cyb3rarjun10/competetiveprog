# Last updated: 3/29/2026, 8:06:17 AM
1class Solution:
2    def firstMatchingIndex(self, s: str) -> int:
3        n=len(s)
4        for i in range(n):
5            if s[i]==s[n-i-1]:
6                return i
7        return -1