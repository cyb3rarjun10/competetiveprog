# Last updated: 3/7/2026, 7:20:37 PM
1class Solution:
2    def minDistance(self, word1: str, word2: str) -> int:
3        w1=len(word1)
4        w2=len(word2)
5        n=len(word1)
6        @cache
7        def dp(i,j):
8            if i==w1 and j!=w2:
9                return (w2-j) 
10            if j==w2 and i!=w1:
11                return (w1-i) 
12            if i==w1 and j==w2:
13                return 0
14            if word1[i]==word2[j]:
15                return dp(i+1,j+1)
16            replace=1+(dp(i+1,j+1))
17            delete=1+dp(i+1,j)
18            insert=1+dp(i,j+1)
19            return min(replace,delete,insert)
20        return dp(0,0)
21            
22            
23        
24
25
26