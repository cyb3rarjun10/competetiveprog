# Last updated: 3/28/2026, 8:24:05 PM
1class Solution:
2    def countVisiblePeople(self, n: int, pos: int, k: int) -> int:
3        mod=(10**9)+7
4        k=min(k,n-1-k)
5        nr=1
6        dr=1
7        for i in range(k):
8            nr=(nr*(n-1-i))%mod
9            dr=(dr*(i+1))%mod
10
11        comb=(nr*pow(dr,mod-2,mod))%mod
12        return (comb*2)%mod