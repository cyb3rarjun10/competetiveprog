# Last updated: 3/5/2026, 2:47:35 PM
1class Solution:
2    def longestPalindrome(self, s: str) -> str:
3        n=len(s)
4        maxolen=0
5        maxol=0
6        maxor=0
7        for i in range(n):
8            l=i
9            r=i
10            while l>=0 and r<n and s[l]==s[r]:
11                if r-l +1 > maxolen:
12                    maxolen=r-l+1
13                    maxol=l
14                    maxor=r    
15                l-=1
16                r+=1
17        maxelen=0
18        maxel=0
19        maxer=0
20        for i in range(n-1):
21            l=i
22            r=i+1
23            while l>=0 and r<n and s[l]==s[r]:
24                if r-l +1 > maxelen:
25                    maxelen=r-l+1
26                    maxel=l
27                    maxer=r
28                l-=1
29                r+=1
30        fl=0
31        fr=0
32        if maxelen>maxolen:
33            fl=maxel
34            fr=maxer
35        else:
36            fl=maxol
37            fr=maxor
38        return s[fl:fr+1]
39
40# class Solution:
41#     def longestPalindrome(self, s: str) -> str:
42#         if len(s) <= 1:
43#             return s
44
45#         def expand_from_center(left, right):
46#             while left >= 0 and right < len(s) and s[left] == s[right]:
47#                 left -= 1
48#                 right += 1
49#             return s[left + 1:right]
50
51#         max_str = s[0]
52
53#         for i in range(len(s) - 1):
54#             odd = expand_from_center(i, i)
55#             even = expand_from_center(i, i + 1)
56
57#             if len(odd) > len(max_str):
58#                 max_str = odd
59#             if len(even) > len(max_str):
60#                 max_str = even
61
62#         return max_str        
63            