# Last updated: 3/28/2026, 4:26:39 PM
1class Solution:
2    def longestPalindromeSubseq(self, s: str) -> int:
3        n=len(s)
4        @cache
5        def recurse(i,j):
6            if i>j:
7                return 0
8            if i==j:
9                return 1
10            elif s[i]==s[j]:
11                return 2+recurse(i+1,j-1)
12            else:
13                return max(recurse(i+1,j),recurse(i,j-1))
14        return recurse(0,n-1)