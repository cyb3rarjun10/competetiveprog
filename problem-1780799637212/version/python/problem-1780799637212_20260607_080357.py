# Last updated: 6/7/2026, 8:03:57 AM
1class Solution:
2    def sumOfGoodIntegers(self, n: int, k: int) -> int:
3        lb=max(1,n-k)
4        ub=n+k
5        res=0
6        for i in range(lb,ub+1):
7            if (n&i)==0:
8                res+=i
9        return res