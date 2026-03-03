# Last updated: 3/3/2026, 2:09:59 PM
1class Solution:
2    def findKthBit(self, n: int, k: int) -> str:
3        def invert(s):
4            res=""
5            for i in s:
6                if i=="0":
7                    res+="1"
8                else:
9                    res+="0"
10            return res[::-1]
11        def recurse(n,s):
12            if n<=1:
13                return s
14            y=recurse(n-1,s+"1"+invert(s))
15            return y
16        x=recurse(n,"0")
17        return x[k-1]
18        
19
20
21