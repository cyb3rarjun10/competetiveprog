# Last updated: 3/1/2026, 2:07:13 PM
1class Solution:
2    def minPartitions(self, n: str) -> int:
3        maxdigit=-1
4        for i in n:
5            if int(i)>maxdigit:
6                maxdigit=int(i)
7        return maxdigit