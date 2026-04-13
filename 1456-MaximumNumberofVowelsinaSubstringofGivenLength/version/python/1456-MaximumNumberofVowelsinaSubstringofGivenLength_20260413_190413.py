# Last updated: 4/13/2026, 7:04:13 PM
1class Solution:
2    def maxVowels(self, s: str, k: int) -> int:
3        prearr=[0]
4        vowel={'a','e','i','o','u'}
5        c=0
6        for i in s:
7            if i in vowel:
8                c+=1
9            prearr.append(c)
10        res=float('-inf')
11        for i in range(k,len(prearr)):
12            res=max(res,prearr[i]-prearr[i-k])
13        return res
14
15