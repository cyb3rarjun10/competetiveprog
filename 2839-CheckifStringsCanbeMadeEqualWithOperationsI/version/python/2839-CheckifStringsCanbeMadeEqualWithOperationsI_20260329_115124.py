# Last updated: 3/29/2026, 11:51:24 AM
1class Solution:
2    def canBeEqual(self, s1: str, s2: str) -> bool:
3        a = sorted([s1[0], s1[2]])
4        b = sorted([s1[1], s1[3]])
5        c = sorted([s2[0], s2[2]])
6        d = sorted([s2[1], s2[3]])
7        return a == c and b == d