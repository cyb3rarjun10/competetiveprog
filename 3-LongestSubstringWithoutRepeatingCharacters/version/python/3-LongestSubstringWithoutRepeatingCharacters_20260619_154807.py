# Last updated: 6/19/2026, 3:48:07 PM
1class Solution:
2    def lengthOfLongestSubstring(self, s: str) -> int:
3        if s=="":
4            return 0
5        n=len(s)
6        if n==1:
7            return 1
8        l=0
9        r=n-1
10        res=-1
11        d=defaultdict(int)
12        for r in range(n):
13            d[s[r]]+=1
14            while l<r and d[s[r]]>1:
15                d[s[l]]-=1
16                l+=1
17            res=max(res, (r-l)+1)
18        return res
19
20