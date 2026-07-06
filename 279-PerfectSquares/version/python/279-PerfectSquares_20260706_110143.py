# Last updated: 7/6/2026, 11:01:43 AM
1class Solution:
2    def numSquares(self, n: int) -> int:
3        squares=[]
4        i=1
5        while i*i <=n:
6            squares.append(i*i)
7            i+=1
8        
9        @cache
10        def dp(rem):
11            if rem==0:
12                return 0
13
14            localmin=float('inf') #minimum in the forloop states
15            for sq in squares:
16                if sq>rem:
17                    break
18                take=1+dp(rem-sq)
19                localmin=min(localmin,take)
20
21            return localmin
22
23        return dp(n)
24
25            