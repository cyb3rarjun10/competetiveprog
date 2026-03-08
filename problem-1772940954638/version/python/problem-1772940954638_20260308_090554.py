# Last updated: 3/8/2026, 9:05:54 AM
1class Solution:
2    def minCost(self, s: str, encCost: int, flatCost: int) -> int:
3        n=len(s)
4        ones=[0]
5        c=0
6        for i in s:
7            if i=="1":
8                c+=1
9            ones.append(c)  
10        @lru_cache
11        def recurse(l,r):
12            x=ones[r]-ones[l]
13            if x==0:
14                cost=flatCost
15            else:
16                cost=(r-l)*x*encCost
17            if (r-l)%2!=0:
18                return cost
19            mid=(l+r)//2
20            splitcost=recurse(l,mid)+recurse(mid,r)
21            return min(cost,splitcost)
22        return recurse(0,n)
23            