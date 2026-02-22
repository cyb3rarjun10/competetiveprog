# Last updated: 2/22/2026, 8:16:37 AM
1class Solution:
2    def isDigitorialPermutation(self, n: int) -> bool:
3        def factorial(n):
4            if n == 0 or n == 1:
5                return 1
6            return n * factorial(n - 1)
7        digits=[]
8        for i in str(n):
9            digits.append(int(i))
10        sd=[]
11        tot=0
12        for num in digits:
13            f=factorial(num)
14            tot+=f
15        for i in str(tot):
16            sd.append(int(i))
17        return sorted(digits)==sorted(sd)
18        
19            
20        