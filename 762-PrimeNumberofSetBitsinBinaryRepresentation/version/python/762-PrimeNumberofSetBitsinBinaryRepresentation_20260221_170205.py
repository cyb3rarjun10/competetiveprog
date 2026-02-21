# Last updated: 2/21/2026, 5:02:05 PM
1class Solution:
2    def countPrimeSetBits(self, left: int, right: int) -> int:
3        prime=set({2,3,5,7,11,13,17,19})
4        def countsetbits(num):
5            b=str(bin(num))
6            c=0
7            for i in b:
8                if i=="1":
9                    c+=1
10            return c
11        res=0
12        for i in range(left,right+1):
13            setbits=countsetbits(i)
14            if setbits in prime:
15                res+=1
16        return res
17
18        